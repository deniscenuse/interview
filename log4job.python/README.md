# log4job.python

A simple Python application to parse job logs, calculate durations, and generate reports.

This project is part of a coding exercise. It reads `.log` files containing `START` and `END` events, matches them, calculates how long each job ran, and classifies jobs as:
- ✅ **Clean:** finished in under 5 minutes
- ⚠️ **Warning:** ran between 5–10 minutes
- ❌ **Error:** ran longer than 10 minutes

The app generates separate CSV reports for each category in a timestamped output folder.

---

## 📂 Project structure

<pre> ```text log4job.python/ ├── archive/ # Processed input files are moved here ├── input/ # Place your .log files here ├── output/ # Reports are generated here ├── lib/ # Core logic split into modules │ ├── file_utils.py │ ├── job_processor.py │ ├── report_writer.py │ └── time_utils.py ├── main.py # Entry point └── README.md ``` </pre>

---

## 🚀 How to run

1️⃣ Install Python 3 (tested with 3.10+).

2️⃣ Place your `.log` file(s) in the `input/` folder.  
   Example line format: 11:35:23,scheduled task 032, START,37980
   
3️⃣ Run the app from inside `log4job.python` folder:
```bash
python3 main.py

```