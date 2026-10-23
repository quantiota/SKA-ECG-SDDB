"""Sudden Cardiac Death Holter record reader — the data source for the SDDB stream.

Turns SDDB WFDB records (header + format-212 binary, 2 ECG leads) into a sequence of samples
of the first lead, at the native rate (250 Hz):

    sample k  =  the ECG at t = k / 250 s
    value     =  (adc - baseline) / gain     in mV, from the record header

Format 212: two 12-bit samples packed in 3 bytes, the signals interleaved.
Records are emitted one after another, each whole. Raw values only: no
resampling, no filtering, no beat detection, no scaling.
"""
from __future__ import annotations

import pathlib

import numpy as np


def read_header(path):
    """SDDB .hea -> fs, n, the signals (file, fmt, gain, baseline) and the comment lines."""
    text = pathlib.Path(path).read_text().splitlines()
    lines = [l for l in text if l.strip() and not l.startswith('#')]
    _, nsig, fs, n = lines[0].split()[:4]
    signals = []
    for l in lines[1:1 + int(nsig)]:
        f = l.split()
        signals.append({'file': f[0], 'fmt': f[1], 'gain': float(f[2]), 'baseline': float(f[4])})
    comments = [l[1:].strip() for l in text if l.startswith('#')]
    return {'nsig': int(nsig), 'fs': float(fs), 'n': int(n), 'signals': signals, 'comments': comments}


def read_212(path, nsig):
    """Format 212 -> int array (samples, nsig)."""
    b = np.fromfile(path, dtype=np.uint8)
    b = b[: b.size - b.size % 3].reshape(-1, 3).astype(np.int32)
    s0 = b[:, 0] | ((b[:, 1] & 0x0F) << 8)
    s1 = b[:, 2] | ((b[:, 1] & 0xF0) << 4)
    s = np.column_stack([s0, s1]).ravel()
    s[s > 2047] -= 4096                                     # 12-bit two's complement
    return s[: s.size - s.size % nsig].reshape(-1, nsig)


def read_records(path):
    """records.txt -> [{name, record_id, sex, age, rhythm, vf_onset}], in order ('#' lines ignored)."""
    out = []
    for l in pathlib.Path(path).read_text().splitlines():
        if l.strip() and not l.startswith('#'):
            f = l.split()
            out.append(dict(name=f[0], record_id=f[1], sex=f[2], age=f[3], rhythm=f[4], vf_onset=f[5]))
    return out


def vf_onset_s(rec):
    """VF onset in seconds from the start of the recording, or None."""
    if rec['vf_onset'] == 'none':
        return None
    h, m, s = (int(v) for v in rec['vf_onset'].split(':'))
    return 3600 * h + 60 * m + s


class SDDBRecord:
    """One record, the first ECG lead, whole."""

    def __init__(self, data_dir, rec, channel=0):
        self.record_id = rec['record_id']
        self.info = rec
        hdr = read_header(pathlib.Path(data_dir) / f"{rec['name']}.hea")
        sig = hdr['signals'][channel]
        if sig['fmt'] != '212':
            raise SystemExit(f'record {self.record_id}: format {sig["fmt"]} not supported')
        self.fs, self.gain, self.baseline = hdr['fs'], sig['gain'], sig['baseline']
        raw = read_212(pathlib.Path(data_dir) / sig['file'], hdr['nsig'])
        if len(raw) != hdr['n']:
            raise SystemExit(f'record {self.record_id}: header says {hdr["n"]:,} samples, '
                             f'file holds {len(raw):,}')
        self.adc = raw[:, channel].astype(np.int64)

    @property
    def n(self):
        return int(self.adc.size)

    def value(self):
        """The samples in mV."""
        return (self.adc - self.baseline) / self.gain


class SDDBChain:
    """Walks the listed records and yields one event per sample."""

    def __init__(self, data_dir, records, channel=0, max_steps=None):
        self.records = [SDDBRecord(data_dir, r, channel) for r in records]
        self.max_steps = max_steps

    @property
    def total_steps(self):
        return sum(r.n for r in self.records)

    def events(self):
        step = 0
        for rec in self.records:
            v = rec.value()
            for k in range(rec.n):
                if self.max_steps is not None and step >= self.max_steps:
                    return
                yield {'step': step, 'record_id': rec.record_id, 'age_band': rec.info['age'],
                       'sample_index': k, 'record_length': rec.n,
                       'adc': int(rec.adc[k]), 'value': float(v[k])}
                step += 1


if __name__ == '__main__':
    from config import ECG_CONFIG as C
    for rec in read_records(C['records']):
        r = SDDBRecord(C['data_dir'], rec, C['channel'])
        v = r.value()
        print(f"{r.record_id}  {rec['sex']} {rec['age']}  {rec['rhythm']}  {r.fs:g} Hz  {r.n:,} samples "
              f"({r.n / r.fs / 3600:.2f} h)  VF {rec['vf_onset']}  {v.min():+.3f} .. {v.max():+.3f} mV")
