#!/usr/bin/env python3
"""Figures and the three cubes (plain, tagged, Δt) of every exported loop of a record that has none yet.

    results/<id>/<loop>/figures/            plot_record.py
    vr/<id>/ska_ecg_<loop>_scale<s>_vr.html, _tagged_vr.html, _dt_vr.html

    python loop_outputs.py 52
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "ecg-data-validation"))
from sddb_chain import read_records                               # noqa: E402

CUBES = [("ska_ecg_vr_template.html", "", None), ("ska_ecg_vr_template_tagged.html", "_tagged", "tagged"),
         ("ska_ecg_vr_template_dt.html", "_dt", "dt")]


def main():
    rid = sys.argv[1]
    scale = float(sys.argv[2]) if len(sys.argv) > 2 else 25.0
    info = {r["record_id"]: r for r in read_records(HERE.parent / "ecg-data-validation" / "records.txt")}[rid]
    who = f"{info['sex']}, {info['age']}"
    vr = HERE / "vr" / rid
    vr.mkdir(parents=True, exist_ok=True)
    for runs in sorted((HERE / "results" / rid).glob(f"{rid}_L*/ska_{rid}_L*_runs.csv")):
        lid = runs.parent.name
        if not (runs.parent / "figures" / f"bands3d_{lid}_cdot_cos_scale{scale:g}.png").exists():
            subprocess.run([sys.executable, "plot_record.py", rid, lid, str(scale)], cwd=HERE, check=True,
                           stdout=subprocess.DEVNULL)
        for tpl, suffix, mode in CUBES:
            out = vr / f"ska_ecg_{lid}_scale{scale:g}{suffix}_vr.html"
            if not out.exists():
                subprocess.run([sys.executable, "build_ecg_vr.py", tpl, str(runs), str(scale), who, str(out)]
                               + ([mode] if mode else []), cwd=HERE, check=True, stdout=subprocess.DEVNULL)
        print(f"[out]    {lid}", flush=True)


if __name__ == "__main__":
    main()
