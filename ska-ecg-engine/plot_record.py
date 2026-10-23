#!/usr/bin/env python3
"""Figures for one loop of one record and one scale (as plot_record.py of SKA-ECG-Fantasia).

    results/<id>/<loop>/figures/ska_<loop>_cdot_cos_scale<s>.png      entropy H and P = exp(-|ΔH/H|) on the step index
    results/<id>/<loop>/figures/bands3d_<loop>_cdot_cos_scale<s>.png  the steps in the learner's space (z, ż, P)

Colour = the transition between two successive waves (P→Q, Q→R, R→S, S→T, T→P).
The title gives the time of the loop in the recording and the VF onset (PhysioNet).

    python plot_record.py 52 52_L000 25
"""
import pathlib
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent
VAL = HERE.parent / "ecg-data-validation"
sys.path.insert(0, str(VAL))
from sddb_chain import read_records                               # noqa: E402
NAMES = ["P→Q", "Q→R", "R→S", "S→T", "T→P"]
COLORS = ["#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#3987e5"]


def hms(s):
    s = int(s)
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def main():
    rid, lid, scale = sys.argv[1], sys.argv[2], float(sys.argv[3])
    d = pd.read_csv(HERE / "results" / rid / lid / f"ska_{lid}_runs.csv", dtype={"record_id": str})
    d = d[(d.input == "cdot_cos") & (d.scale == scale)].sort_values("event_index")
    t0, t1 = d.peak.iloc[0] / 1000, d.peak.iloc[-1] / 1000
    d = d[np.isfinite(d.zdot)]
    d["tr"] = d.transition.str.replace("-", "→")
    info = {r["record_id"]: r for r in read_records(VAL / "records.txt")}[rid]
    out = HERE / "results" / rid / lid / "figures"
    out.mkdir(parents=True, exist_ok=True)
    title = (f"Record {rid}, loop {lid.split('_')[-1]} ({hms(t0)}–{hms(t1)}; VF onset {info['vf_onset']}) "
             f"(SDDB, {info['sex']}, {info['age']}), input Re ċ, scale {scale:g}")

    fig, ax = plt.subplots(2, 1, figsize=(12, 7), sharex=True)
    for name, color in zip(NAMES, COLORS):
        m = d.tr == name
        ax[0].scatter(d.event_index[m], d.entropy[m], s=2, color=color, label=name)
        ax[1].scatter(d.event_index[m], d.P[m], s=2, color=color)
    ax[0].set_ylabel("entropy H")
    ax[1].set_ylabel("P = exp(−|ΔH/H|)")
    ax[1].set_xlabel("step")
    ax[0].legend(markerscale=5, ncol=5, loc="upper right", fontsize=8)
    ax[0].set_title(title)
    f1 = out / f"ska_{lid}_cdot_cos_scale{scale:g}.png"
    fig.savefig(f1, dpi=140, bbox_inches="tight"); plt.close(fig)

    fig = plt.figure(figsize=(9, 8))
    ax = fig.add_subplot(projection="3d")
    for name, color in zip(NAMES, COLORS):
        m = d.tr == name
        ax.scatter(d.knowledge[m], d.zdot[m], d.P[m], s=3, color=color, label=name, edgecolors="none")
    ax.set_xlabel("z = ‖Z‖"); ax.set_ylabel("ż (1/s)"); ax.set_zlabel("P")
    ax.legend(markerscale=4, fontsize=8)
    ax.set_title(title, fontsize=9)
    f2 = out / f"bands3d_{lid}_cdot_cos_scale{scale:g}.png"
    fig.savefig(f2, dpi=140, bbox_inches="tight"); plt.close(fig)
    print(f"[png]    {f1}\n[png]    {f2}")


if __name__ == "__main__":
    main()
