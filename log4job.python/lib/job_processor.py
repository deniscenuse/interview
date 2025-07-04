from lib.time_utils import convert_to_seconds, handle_day_wraparound, format_duration
from lib.report_writer import write_report_line

def process_job_file(input_file, output_dir, timestamp, source_name):
    start_times = {}
    job_names = {}

    with open(input_file, 'r') as f:
        for line in f:
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) != 4:
                continue

            time_str, name, event, pid = parts
            key = f"{name}_{pid}"

            if event == "START":
                start_times[key] = time_str
                job_names[key] = name

            elif event == "END":
                if key not in start_times:
                    continue

                start_time = start_times[key]
                start_sec = convert_to_seconds(start_time)
                end_sec = convert_to_seconds(time_str)
                end_sec = handle_day_wraparound(start_sec, end_sec)
                duration = end_sec - start_sec
                duration_fmt = format_duration(duration)

                if duration > 600:
                    level = "error"
                elif duration > 300:
                    level = "warning"
                else:
                    level = "clean"

                write_report_line(level, name, pid, start_time, time_str, duration_fmt, source_name, output_dir, timestamp)

                del start_times[key]
                del job_names[key]
