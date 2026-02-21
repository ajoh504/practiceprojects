#!python3
# run_itself.py - Write a script that runs itself.
#
#                 1. Check if scheduled task exists first. If not, create it
#                 2. Test the output by writing to a log file
#
#                 USAGE: Place this Python script in user's home directory


import subprocess
from pathlib import Path
from datetime import datetime


def main():
    path_to_log = Path.home() / "log.txt"
    path_to_py_script = Path.home() / "run_itself.py"

    def schedule_task():
        """
        Use SCHTASKS /Query in cmd.exe to check if the task exists. If it does not,
        create it using SCHTASKS /Create.
        """
        with subprocess.Popen(
            ["cmd.exe", "SCHTASKS /Query /TN 'Run Itself'"],
            stderr=subprocess.PIPE,
        ) as process:
            if process.stderr is not None:
                subprocess.run(
                    [
                        "cmd.exe",
                        f"SCHTASKS /CREATE /SC MINUTE /MO 1 /ST 20:00 /TN \"Run Itself\" /TR \"{path_to_py_script}\"",
                    ],
                )

    def write_to_log():
        """Log the date and time showing when the script ran."""
        with open(path_to_log, "a") as f:
            f.write(datetime.now().strftime("%A %B %Y %I:%M %p\n"))

    #schedule_task()
    write_to_log()


if __name__ == "__main__":
    main()
