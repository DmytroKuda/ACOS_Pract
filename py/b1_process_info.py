import os
import subprocess

pid = os.getpid()
ppid = os.getppid()

print(f"Python PID: {pid}")
print(f"Python PPID: {ppid}")
print("\nProcess info from ps:")
subprocess.run(["ps", "-p", str(pid), "-o", "pid,ppid,stat,ni,comm"])
