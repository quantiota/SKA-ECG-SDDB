# SKA ECG SDDB

 [![arXiv](https://img.shields.io/badge/arXiv-2503.13942-b31b1b)](https://arxiv.org/abs/2503.13942)   [![arXiv](https://img.shields.io/badge/arXiv-2504.03214-b31b1b)](https://arxiv.org/abs/2504.03214)   [![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-SKA-orange)](https://huggingface.co/quant-iota) [![Sponsor](https://img.shields.io/badge/Sponsor-quantiota-ea4aaa?logo=github-sponsors)](https://github.com/sponsors/quantiota)


**Structured Knowledge Accumulation (SKA) on the hours before and after a ventricular arrhythmia**

This project applies the SKA real-time learner to long Holter recordings from the PhysioNet
[Sudden Cardiac Death Holter Database](https://physionet.org/content/sddb/1.0.0/) (SDDB;
Greenwald S.D., *Development and analysis of a ventricular fibrillation detector*, M.S. thesis, MIT, 1986;
[doi:10.13026/C2W306](https://doi.org/10.13026/C2W306); Open Data Commons Attribution License v1.0).

The method is the one of
[SKA-ECG-Heart-Rate-Variability](https://github.com/quantiota/SKA-ECG-Heart-Rate-Variability):
the five waves of each cardiac cycle, the same input, the same learner, the same 3D cube.

## Data

23 Holter recordings (records 30–52), mainly from the 1980s in Boston-area hospitals, 2 ECG leads at
250 Hz, 4 to 25 hours each. 18 patients were in sinus rhythm (4 with intermittent pacing), 1 was
continuously paced and 4 were in atrial fibrillation. All had a sustained ventricular tachyarrhythmia
during the recording, and most had an actual cardiac arrest. The time of VF onset is given for each
record by PhysioNet.

## Successive loops

Each record is learned whole, as successive loops: the waves of the whole recording (first lead) are
cut into loops of 3,500 steps (700 cycles), and each loop is learned by a fresh learner, as a
standard run, at scale 25. The loops before, during and after the VF onset can then be compared.

| record | sex, age | rhythm | duration | VF onset | loops |
|---|---|---|---|---|---|
| 52 | F, 82 | sinus | 07:31:05 | 02:32:40 (loop 019) | 60 |

## Folders

| folder | content |
|---|---|
| [`ecg-data-validation/`](ecg-data-validation/) | the SDDB records: download, reader, stream into QuestDB |
| [`ska-ecg-engine/`](ska-ecg-engine/) | the results, the figures and the cube builder |
| [`vr-library/`](vr-library/) | the cubes |

The SKA real-time engine is proprietary and is not included in this repository.

## License

MIT. ECG data: from PhysioNet, under the license of the Sudden Cardiac Death Holter Database; cite the
database when you use it.
