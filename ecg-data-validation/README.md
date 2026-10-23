# The SDDB records

Source: [Sudden Cardiac Death Holter Database](https://physionet.org/content/sddb/1.0.0/), PhysioNet,
Open Data Commons Attribution License v1.0 — Greenwald S.D., "Development and analysis of a ventricular
fibrillation detector", M.S. thesis, MIT Dept. of Electrical Engineering and Computer Science (1986),
doi:10.13026/C2W306.

```
./fetch_data.sh                      # the records of records.txt -> data/ (not committed)
python sddb_chain.py                 # check: patient, rate, length, VF onset, range of each record
python stream_sddb.py --records 52 --speed 60
```

| file | content |
|---|---|
| `records.txt` | the 23 records, with sex, age, rhythm and VF onset from the PhysioNet page |
| `fetch_data.sh` | downloads the header, signal and beat annotation files of each record |
| `sddb_chain.py` | reads a record (format 212) and gives its first ECG lead in mV, at 250 Hz |
| `stream_sddb.py` | streams the ECG into the QuestDB table `ecg_sddb_steps`, at 250 Hz, the whole record |
| `config.py` | QuestDB connection and stream settings |
