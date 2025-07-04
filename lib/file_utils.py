import os
import shutil


def archive_input_file(input_path, archive_dir, timestamp):
    os.makedirs(archive_dir, exist_ok=True)
    base_name = os.path.basename(input_path)
    new_name = f"logs_{timestamp}_{base_name}"
    target_path = os.path.join(archive_dir, new_name)
    shutil.move(input_path, target_path)
