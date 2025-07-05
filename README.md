# Denis-Ionut Cenuse — DevOps Engineer Candidate

Hello! My name is **Denis**, and I’m applying for the **DevOps Engineer position** within the *Engineering Excellence & Productivity (EXP)* team within London Stock Exchange Group.

I’m a cloud enthusiast and I want to evolve my skills into the DevOps world. 

For this coding exercise, I’ve built two implementations of a **log processing application**: one in **Bash** and one in **Python**. Both applications have reached their final form on the date of 5th of July. 
The task was to analyze log files with `START` and `END` events, calculate job durations, classify them based on thresholds, and generate clean, machine-readable reports.  

---

## 📝 Why Bash and Python?

I chose to implement both **Bash** and **Python** because they each offer unique advantages in a DevOps context:

✅ **Bash:**
- Already available on almost every Linux/Unix system by default — no dependencies.
- Very lightweight and great for quick, portable scripts.
- Ideal for chaining together standard tools, moving files, and gluing together pipelines.

✅ **Python:**
- Easy to write and maintain even as complexity grows.
- Better for structured data processing (CSV, JSON).
- A go-to language for automation beyond basic scripting, and integrates well with cloud SDKs and APIs.

---

# 📂 log4job — the Application

This repository contains two implementations of the `log4job` application:

- [`log4job.bash`](./log4job.bash) — written in Bash, demonstrating intermediate shell scripting practices.
- [`log4job.python`](./log4job.python) — written in Python, demonstrating modular, maintainable code.

Both implementations solve the same problem:  
✔️ Read job log files  
✔️ Track job start and end times  
✔️ Calculate durations  
✔️ Classify jobs into `clean`, `warning`, or `error`  
✔️ Generate CSV reports  
✔️ Archive processed logs