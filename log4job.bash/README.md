# log4job.bash

A Bash implementation of a job log parser and reporter.  
This script reads `.log` files with `START` and `END` events, calculates job durations, classifies jobs, and generates clean CSV reports.

The Bash version is aimed at intermediate users who are comfortable in the shell and familiar with basic scripting concepts, but it remains easy to follow and adapt.

---

## 📂 Project structure

```
log4job.bash/
├── archive/ # Processed input files are moved here
├── input/ # Place your .log files here
├── output/ # Reports and debug logs are generated here
├── lib/ # Modular shell functions
│ ├── file_utils.sh
│ ├── job_processor.sh
│ ├── report_writer.sh
│ └── time_utils.sh
├── main.sh # Entry point
└── README.md
```

---

## 🛠 Features

✅ Calculates job durations in `HH:MM:SS`  
✅ Classifies jobs:
- `clean` if ≤ 5 minutes
- `warning` if > 5 minutes and ≤ 10 minutes
- `error` if > 10 minutes

✅ Generates CSV reports with: level, job name, PID, start time, end time, duration, source file  
✅ Automatically moves processed log files into `archive/` with timestamped names  
✅ Logs processing steps in `output/<timestamp>/debug.log` for easy troubleshooting

---

## 🚀 How to run

1️⃣ Make sure you’re on a Unix-like system (Linux, macOS, WSL).  
2️⃣ Make sure the scripts are executable (`dos2unix main.sh lib/*.sh`).  
3️⃣ Place your `.log` files in the `input/` folder.  
   Example line format: 11:35:23,scheduled task 032, START,37980

4️⃣ Run the script from inside `log4job.bash`:
```bash
./main.sh
```

It will process all .log files in input/, archive them, and write reports to output/<timestamp>/.

You can also process a specific file directly:
```
./main.sh input/yourfile.log
```
## 📝 Notes
- The Bash version is split into modular libraries (lib/*.sh) for clarity and maintainability;
- main.sh is the entry point — it wires together the logic;
- Debug logs are written to output/<timestamp>/debug.log to help trace execution;
- Reports are CSV, so they can easily be opened in Excel or processed further.
