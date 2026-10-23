# SKA learning on the SDDB Holter recordings — results

This folder holds the **results** of the SKA engine on the PhysioNet
[Sudden Cardiac Death Holter Database](../ecg-data-validation/): the learner's output for every step, the figures and the
cubes. The method is that of
[SKA-ECG-Heart-Rate-Variability](https://github.com/quantiota/SKA-ECG-Heart-Rate-Variability/tree/main/ska-ecg-engine):
five waves per cardiac cycle (P, Q, R, S, T), one step per wave, input Re ċ (cosine), scale 25, at 250 Hz.
Each record is learned whole, as successive loops of 3,500 steps (700 cycles), each loop by a fresh learner.
The ECG is streamed into QuestDB (`ecg_sddb_steps`) and the learner's output is stored in
`ecg_sddb_ska_results`, one record_id per loop (`<record>_L<nnn>`). The engine code is not published.

| file | content |
|---|---|
| `results/<id>/<id>_L<nnn>/ska_<id>_L<nnn>_runs.csv` | the learner's output for every step of the loop |
| `results/<id>/<id>_L<nnn>/figures/` | H and P on the step index; the steps in (z, ż, P) |
| `results/<id>/loops.csv` | start and end of each loop (s from the start of the recording), VF onset before, inside or after it |
| `results/<id>/tau_H.csv` | τ_H and N_H of every loop |
| `vr/<id>/` | three cubes per loop (P, missing waves tagged, Δt) |
| `build_ecg_vr.py`, `ska_ecg_vr_template*.html` | the cube builder and its templates |
| `plot_record.py`, `loop_outputs.py`, `tau_h.py` | the figures, the cubes of every loop, τ_H / N_H, from the run CSVs |

τ_H = time for the learner to reach 90 % of its saturation on its slowest transition;
N_H = τ_H / T_c, in cardiac cycles; T_c = mean cycle time of the loop.

## Record 52 (F, 82, sinus rhythm, VF onset 02:32:40)

| loop | time in the recording | VF onset | T_c (ms) | τ_H (min) | N_H (cycles) | figures | cube |
|---|---|---|---|---|---|---|---|
| L000 | 00:00:00–00:07:34 | later | 648 | 7.3 | 673 | [H, P](results/52/52_L000/figures/ska_52_L000_cdot_cos_scale25.png) · [3D](results/52/52_L000/figures/bands3d_52_L000_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L000_scale25_vr.html) |
| L001 | 00:07:35–00:15:01 | later | 637 | 7.3 | 688 | [H, P](results/52/52_L001/figures/ska_52_L001_cdot_cos_scale25.png) · [3D](results/52/52_L001/figures/bands3d_52_L001_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L001_scale25_vr.html) |
| L002 | 00:15:01–00:22:27 | later | 636 | 7.3 | 689 | [H, P](results/52/52_L002/figures/ska_52_L002_cdot_cos_scale25.png) · [3D](results/52/52_L002/figures/bands3d_52_L002_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L002_scale25_vr.html) |
| L003 | 00:22:27–00:30:05 | later | 653 | 5.3 | 485 | [H, P](results/52/52_L003/figures/ska_52_L003_cdot_cos_scale25.png) · [3D](results/52/52_L003/figures/bands3d_52_L003_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L003_scale25_vr.html) |
| L004 | 00:30:06–00:37:37 | later | 644 | 5.8 | 542 | [H, P](results/52/52_L004/figures/ska_52_L004_cdot_cos_scale25.png) · [3D](results/52/52_L004/figures/bands3d_52_L004_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L004_scale25_vr.html) |
| L005 | 00:37:37–00:45:28 | later | 672 | 6.0 | 536 | [H, P](results/52/52_L005/figures/ska_52_L005_cdot_cos_scale25.png) · [3D](results/52/52_L005/figures/bands3d_52_L005_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L005_scale25_vr.html) |
| L006 | 00:45:28–00:53:03 | later | 648 | 6.5 | 603 | [H, P](results/52/52_L006/figures/ska_52_L006_cdot_cos_scale25.png) · [3D](results/52/52_L006/figures/bands3d_52_L006_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L006_scale25_vr.html) |
| L007 | 00:53:03–01:00:47 | later | 662 | 5.4 | 493 | [H, P](results/52/52_L007/figures/ska_52_L007_cdot_cos_scale25.png) · [3D](results/52/52_L007/figures/bands3d_52_L007_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L007_scale25_vr.html) |
| L008 | 01:00:47–01:08:12 | later | 634 | 5.0 | 478 | [H, P](results/52/52_L008/figures/ska_52_L008_cdot_cos_scale25.png) · [3D](results/52/52_L008/figures/bands3d_52_L008_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L008_scale25_vr.html) |
| L009 | 01:08:12–01:16:13 | later | 686 | 5.0 | 437 | [H, P](results/52/52_L009/figures/ska_52_L009_cdot_cos_scale25.png) · [3D](results/52/52_L009/figures/bands3d_52_L009_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L009_scale25_vr.html) |
| L010 | 01:16:13–01:24:41 | later | 724 | 5.0 | 413 | [H, P](results/52/52_L010/figures/ska_52_L010_cdot_cos_scale25.png) · [3D](results/52/52_L010/figures/bands3d_52_L010_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L010_scale25_vr.html) |
| L011 | 01:24:41–01:32:50 | later | 697 | 6.1 | 527 | [H, P](results/52/52_L011/figures/ska_52_L011_cdot_cos_scale25.png) · [3D](results/52/52_L011/figures/bands3d_52_L011_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L011_scale25_vr.html) |
| L012 | 01:32:50–01:40:21 | later | 643 | 5.8 | 539 | [H, P](results/52/52_L012/figures/ska_52_L012_cdot_cos_scale25.png) · [3D](results/52/52_L012/figures/bands3d_52_L012_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L012_scale25_vr.html) |
| L013 | 01:40:21–01:47:51 | later | 642 | 4.7 | 435 | [H, P](results/52/52_L013/figures/ska_52_L013_cdot_cos_scale25.png) · [3D](results/52/52_L013/figures/bands3d_52_L013_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L013_scale25_vr.html) |
| L014 | 01:47:51–01:55:12 | later | 629 | 5.7 | 540 | [H, P](results/52/52_L014/figures/ska_52_L014_cdot_cos_scale25.png) · [3D](results/52/52_L014/figures/bands3d_52_L014_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L014_scale25_vr.html) |
| L015 | 01:55:12–02:02:36 | later | 634 | 4.8 | 458 | [H, P](results/52/52_L015/figures/ska_52_L015_cdot_cos_scale25.png) · [3D](results/52/52_L015/figures/bands3d_52_L015_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L015_scale25_vr.html) |
| L016 | 02:02:37–02:10:13 | later | 652 | 5.7 | 528 | [H, P](results/52/52_L016/figures/ska_52_L016_cdot_cos_scale25.png) · [3D](results/52/52_L016/figures/bands3d_52_L016_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L016_scale25_vr.html) |
| L017 | 02:10:14–02:17:58 | later | 663 | 6.2 | 561 | [H, P](results/52/52_L017/figures/ska_52_L017_cdot_cos_scale25.png) · [3D](results/52/52_L017/figures/bands3d_52_L017_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L017_scale25_vr.html) |
| L018 | 02:17:59–02:25:22 | later | 632 | 6.6 | 624 | [H, P](results/52/52_L018/figures/ska_52_L018_cdot_cos_scale25.png) · [3D](results/52/52_L018/figures/bands3d_52_L018_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L018_scale25_vr.html) |
| L019 | 02:25:22–02:32:56 | **inside** | 648 | 4.5 | 416 | [H, P](results/52/52_L019/figures/ska_52_L019_cdot_cos_scale25.png) · [3D](results/52/52_L019/figures/bands3d_52_L019_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L019_scale25_vr.html) |
| L020 | 02:32:56–02:39:47 | earlier | 587 | 4.1 | 420 | [H, P](results/52/52_L020/figures/ska_52_L020_cdot_cos_scale25.png) · [3D](results/52/52_L020/figures/bands3d_52_L020_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L020_scale25_vr.html) |
| L021 | 02:39:47–02:46:01 | earlier | 532 | 4.6 | 513 | [H, P](results/52/52_L021/figures/ska_52_L021_cdot_cos_scale25.png) · [3D](results/52/52_L021/figures/bands3d_52_L021_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L021_scale25_vr.html) |
| L022 | 02:46:01–02:52:20 | earlier | 544 | 4.5 | 499 | [H, P](results/52/52_L022/figures/ska_52_L022_cdot_cos_scale25.png) · [3D](results/52/52_L022/figures/bands3d_52_L022_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L022_scale25_vr.html) |
| L023 | 02:52:21–02:59:14 | earlier | 594 | 3.9 | 396 | [H, P](results/52/52_L023/figures/ska_52_L023_cdot_cos_scale25.png) · [3D](results/52/52_L023/figures/bands3d_52_L023_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L023_scale25_vr.html) |
| L024 | 02:59:14–03:05:42 | earlier | 553 | 6.4 | 693 | [H, P](results/52/52_L024/figures/ska_52_L024_cdot_cos_scale25.png) · [3D](results/52/52_L024/figures/bands3d_52_L024_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L024_scale25_vr.html) |
| L025 | 03:05:42–03:12:24 | earlier | 574 | 6.2 | 652 | [H, P](results/52/52_L025/figures/ska_52_L025_cdot_cos_scale25.png) · [3D](results/52/52_L025/figures/bands3d_52_L025_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L025_scale25_vr.html) |
| L026 | 03:12:25–03:19:03 | earlier | 569 | 6.1 | 646 | [H, P](results/52/52_L026/figures/ska_52_L026_cdot_cos_scale25.png) · [3D](results/52/52_L026/figures/bands3d_52_L026_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L026_scale25_vr.html) |
| L027 | 03:19:03–03:25:42 | earlier | 569 | 5.8 | 609 | [H, P](results/52/52_L027/figures/ska_52_L027_cdot_cos_scale25.png) · [3D](results/52/52_L027/figures/bands3d_52_L027_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L027_scale25_vr.html) |
| L028 | 03:25:43–03:32:25 | earlier | 573 | 6.1 | 642 | [H, P](results/52/52_L028/figures/ska_52_L028_cdot_cos_scale25.png) · [3D](results/52/52_L028/figures/bands3d_52_L028_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L028_scale25_vr.html) |
| L029 | 03:32:25–03:39:11 | earlier | 580 | 6.7 | 694 | [H, P](results/52/52_L029/figures/ska_52_L029_cdot_cos_scale25.png) · [3D](results/52/52_L029/figures/bands3d_52_L029_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L029_scale25_vr.html) |
| L030 | 03:39:11–03:47:06 | earlier | 680 | 6.1 | 539 | [H, P](results/52/52_L030/figures/ska_52_L030_cdot_cos_scale25.png) · [3D](results/52/52_L030/figures/bands3d_52_L030_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L030_scale25_vr.html) |
| L031 | 03:47:06–03:56:38 | earlier | 824 | 6.4 | 464 | [H, P](results/52/52_L031/figures/ska_52_L031_cdot_cos_scale25.png) · [3D](results/52/52_L031/figures/bands3d_52_L031_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L031_scale25_vr.html) |
| L032 | 03:56:38–04:03:41 | earlier | 605 | 5.0 | 493 | [H, P](results/52/52_L032/figures/ska_52_L032_cdot_cos_scale25.png) · [3D](results/52/52_L032/figures/bands3d_52_L032_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L032_scale25_vr.html) |
| L033 | 04:03:41–04:10:55 | earlier | 624 | 4.1 | 393 | [H, P](results/52/52_L033/figures/ska_52_L033_cdot_cos_scale25.png) · [3D](results/52/52_L033/figures/bands3d_52_L033_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L033_scale25_vr.html) |
| L034 | 04:10:55–04:17:28 | earlier | 561 | 4.4 | 469 | [H, P](results/52/52_L034/figures/ska_52_L034_cdot_cos_scale25.png) · [3D](results/52/52_L034/figures/bands3d_52_L034_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L034_scale25_vr.html) |
| L035 | 04:17:29–04:24:09 | earlier | 571 | 6.3 | 658 | [H, P](results/52/52_L035/figures/ska_52_L035_cdot_cos_scale25.png) · [3D](results/52/52_L035/figures/bands3d_52_L035_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L035_scale25_vr.html) |
| L036 | 04:24:09–04:30:55 | earlier | 578 | 5.0 | 518 | [H, P](results/52/52_L036/figures/ska_52_L036_cdot_cos_scale25.png) · [3D](results/52/52_L036/figures/bands3d_52_L036_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L036_scale25_vr.html) |
| L037 | 04:30:55–04:37:46 | earlier | 587 | 6.7 | 682 | [H, P](results/52/52_L037/figures/ska_52_L037_cdot_cos_scale25.png) · [3D](results/52/52_L037/figures/bands3d_52_L037_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L037_scale25_vr.html) |
| L038 | 04:37:46–04:44:36 | earlier | 585 | 6.2 | 631 | [H, P](results/52/52_L038/figures/ska_52_L038_cdot_cos_scale25.png) · [3D](results/52/52_L038/figures/bands3d_52_L038_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L038_scale25_vr.html) |
| L039 | 04:44:37–04:51:30 | earlier | 590 | 6.3 | 643 | [H, P](results/52/52_L039/figures/ska_52_L039_cdot_cos_scale25.png) · [3D](results/52/52_L039/figures/bands3d_52_L039_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L039_scale25_vr.html) |
| L040 | 04:51:31–04:58:10 | earlier | 577 | 3.8 | 398 | [H, P](results/52/52_L040/figures/ska_52_L040_cdot_cos_scale25.png) · [3D](results/52/52_L040/figures/bands3d_52_L040_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L040_scale25_vr.html) |
| L041 | 04:58:10–05:05:02 | earlier | 609 | 5.8 | 570 | [H, P](results/52/52_L041/figures/ska_52_L041_cdot_cos_scale25.png) · [3D](results/52/52_L041/figures/bands3d_52_L041_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L041_scale25_vr.html) |
| L042 | 05:05:02–05:11:56 | earlier | 601 | 5.4 | 543 | [H, P](results/52/52_L042/figures/ska_52_L042_cdot_cos_scale25.png) · [3D](results/52/52_L042/figures/bands3d_52_L042_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L042_scale25_vr.html) |
| L043 | 05:11:56–05:19:05 | earlier | 622 | 5.4 | 523 | [H, P](results/52/52_L043/figures/ska_52_L043_cdot_cos_scale25.png) · [3D](results/52/52_L043/figures/bands3d_52_L043_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L043_scale25_vr.html) |
| L044 | 05:19:05–05:25:39 | earlier | 574 | 3.8 | 402 | [H, P](results/52/52_L044/figures/ska_52_L044_cdot_cos_scale25.png) · [3D](results/52/52_L044/figures/bands3d_52_L044_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L044_scale25_vr.html) |
| L045 | 05:25:39–05:32:11 | earlier | 568 | 4.9 | 516 | [H, P](results/52/52_L045/figures/ska_52_L045_cdot_cos_scale25.png) · [3D](results/52/52_L045/figures/bands3d_52_L045_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L045_scale25_vr.html) |
| L046 | 05:32:11–05:38:48 | earlier | 566 | 6.4 | 676 | [H, P](results/52/52_L046/figures/ska_52_L046_cdot_cos_scale25.png) · [3D](results/52/52_L046/figures/bands3d_52_L046_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L046_scale25_vr.html) |
| L047 | 05:38:48–05:45:55 | earlier | 609 | 5.9 | 585 | [H, P](results/52/52_L047/figures/ska_52_L047_cdot_cos_scale25.png) · [3D](results/52/52_L047/figures/bands3d_52_L047_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L047_scale25_vr.html) |
| L048 | 05:45:55–05:53:01 | earlier | 608 | 6.4 | 628 | [H, P](results/52/52_L048/figures/ska_52_L048_cdot_cos_scale25.png) · [3D](results/52/52_L048/figures/bands3d_52_L048_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L048_scale25_vr.html) |
| L049 | 05:53:01–05:59:57 | earlier | 594 | 5.1 | 517 | [H, P](results/52/52_L049/figures/ska_52_L049_cdot_cos_scale25.png) · [3D](results/52/52_L049/figures/bands3d_52_L049_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L049_scale25_vr.html) |
| L050 | 05:59:57–06:06:50 | earlier | 589 | 5.6 | 565 | [H, P](results/52/52_L050/figures/ska_52_L050_cdot_cos_scale25.png) · [3D](results/52/52_L050/figures/bands3d_52_L050_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L050_scale25_vr.html) |
| L051 | 06:06:50–06:13:29 | earlier | 572 | 6.1 | 638 | [H, P](results/52/52_L051/figures/ska_52_L051_cdot_cos_scale25.png) · [3D](results/52/52_L051/figures/bands3d_52_L051_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L051_scale25_vr.html) |
| L052 | 06:13:29–06:20:39 | earlier | 616 | 4.6 | 452 | [H, P](results/52/52_L052/figures/ska_52_L052_cdot_cos_scale25.png) · [3D](results/52/52_L052/figures/bands3d_52_L052_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L052_scale25_vr.html) |
| L053 | 06:20:39–06:27:38 | earlier | 598 | 6.9 | 694 | [H, P](results/52/52_L053/figures/ska_52_L053_cdot_cos_scale25.png) · [3D](results/52/52_L053/figures/bands3d_52_L053_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L053_scale25_vr.html) |
| L054 | 06:27:38–06:37:17 | earlier | 827 | 6.5 | 470 | [H, P](results/52/52_L054/figures/ska_52_L054_cdot_cos_scale25.png) · [3D](results/52/52_L054/figures/bands3d_52_L054_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L054_scale25_vr.html) |
| L055 | 06:37:17–06:56:17 | earlier | 1626 | 16.0 | 592 | [H, P](results/52/52_L055/figures/ska_52_L055_cdot_cos_scale25.png) · [3D](results/52/52_L055/figures/bands3d_52_L055_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L055_scale25_vr.html) |
| L056 | 06:56:17–07:03:26 | earlier | 612 | 7.1 | 693 | [H, P](results/52/52_L056/figures/ska_52_L056_cdot_cos_scale25.png) · [3D](results/52/52_L056/figures/bands3d_52_L056_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L056_scale25_vr.html) |
| L057 | 07:03:26–07:10:34 | earlier | 611 | 4.7 | 464 | [H, P](results/52/52_L057/figures/ska_52_L057_cdot_cos_scale25.png) · [3D](results/52/52_L057/figures/bands3d_52_L057_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L057_scale25_vr.html) |
| L058 | 07:10:34–07:19:29 | earlier | 764 | 5.0 | 391 | [H, P](results/52/52_L058/figures/ska_52_L058_cdot_cos_scale25.png) · [3D](results/52/52_L058/figures/bands3d_52_L058_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L058_scale25_vr.html) |
| L059 | 07:19:29–07:30:21 | earlier | 931 | 6.6 | 423 | [H, P](results/52/52_L059/figures/ska_52_L059_cdot_cos_scale25.png) · [3D](results/52/52_L059/figures/bands3d_52_L059_cdot_cos_scale25.png) | [cube](vr/52/ska_ecg_52_L059_scale25_vr.html) |
