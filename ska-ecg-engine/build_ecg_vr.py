"""
ECG VR cube for an SDDB loop: fills the Three.js template with one run of the SKA learner.

The template (ska_ecg_vr_template.html) holds two placeholders:
    __DATA__         the points: z, ż, P and the transition of each step
    __DESCRIPTION__  the line under the title (record, subject, cycles, input, scale)

Usage
    python build_ecg_vr.py ska_ecg_vr_template.html ska_<record>_runs.csv <scale> "<subject>" out.html
    python build_ecg_vr.py ska_ecg_vr_template.html ska_f1y01_runs.csv 25 "F, 23" ska_ecg_f1y01_scale25_vr.html
    python build_ecg_vr.py ska_ecg_vr_template_tagged.html ska_f1y01_runs.csv 25 "F, 23" ska_ecg_f1y01_scale25_tagged_vr.html tagged
    python build_ecg_vr.py ska_ecg_vr_template_dt.html ska_f1y01_runs.csv 25 "F, 23" ska_ecg_f1y01_scale25_dt_vr.html dt

With "tagged", a step that goes into or out of a missing wave (value_cos = value_sin = 0) is
marked and drawn as a cross, in its transition colour. With "dt", the vertical axis is Δt, the
time since the previous wave (ms), instead of P.
Requires: numpy, pandas
"""
import json
import sys

import pandas as pd

NAMES = ["P→Q", "Q→R", "R→S", "S→T", "T→P"]
COLORS = ["#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#3987e5"]


def main():
    tpl, csv, scale, subject, out = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4], sys.argv[5]
    tagged = len(sys.argv) > 6 and sys.argv[6] == "tagged"
    dt = len(sys.argv) > 6 and sys.argv[6] == "dt"                    # vertical axis = delta_t (ms), not P
    d = pd.read_csv(csv, dtype={"record_id": str})
    d = d[(d.input == "cdot_cos") & (d.scale == scale)].sort_values("event_index").reset_index(drop=True)
    missing = (d.value_cos == 0) & (d.value_sin == 0)                  # the wave of this step is missing
    d["m"] = (missing | missing.shift(fill_value=False)).astype(int)   # into it, or out of it
    d = d.dropna(subset=["P", "zdot"]).reset_index(drop=True)
    if d.empty:
        raise SystemExit(f"no rows for input=cdot_cos scale={scale:g}")
    rec = str(d.record_id.iloc[0])
    tr = d.transition.str.replace("-", "→")
    D = dict(z=d.knowledge.round(2).tolist(), zd=d.zdot.round(3).tolist(), p=d.P.round(4).tolist(),
             t=[NAMES.index(t) for t in tr], names=NAMES, colors=COLORS,
             zmax=float(d.knowledge.max()), zdmax=float(d.zdot.max()))
    if tagged:
        D["m"] = d.m.tolist()
    if dt:
        D["p"] = (1000 * d.delta_t).round(1).tolist()
        D["ymax"] = float(1000 * d.delta_t.max())
    desc = (f"Loop {rec}, PhysioNet Sudden Cardiac Death Holter Database ({subject}, first ECG lead, 250 Hz), "
            f"{d.k.nunique()} cycles = {len(d):,} steps of SKA real-time learning. "
            f"Input: Re ċ (cosine), scale {scale:g}. Horizontal axes: z = ‖Z‖ and ż = dz/dt (1/s); "
            + ("vertical axis: Δt, the time since the previous wave (ms). " if dt else "vertical axis: P = exp(−|ΔH/H|). ")
            + "5 colours = the five transitions of the cardiac cycle.")
    s = open(tpl, encoding="utf-8").read()
    if "__DATA__" not in s or "__DESCRIPTION__" not in s:
        raise SystemExit("template is missing __DATA__ or __DESCRIPTION__")
    s = s.replace("__DATA__", json.dumps(D, separators=(",", ":"), ensure_ascii=False))
    s = s.replace("__DESCRIPTION__", desc)
    open(out, "w", encoding="utf-8").write(s)
    print(f"saved {out}  (record {rec}, {len(d):,} steps)")


if __name__ == "__main__":
    main()
