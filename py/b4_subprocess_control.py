import subprocess
import time
import signal

proc = subprocess.Popen(["sleep", "100"])
print(f"Started process {proc.pid}")

time.sleep(1)
print("Sending SIGSTOP...")
proc.send_signal(signal.SIGSTOP)

time.sleep(1)
print("Sending SIGCONT...")
proc.send_signal(signal.SIGCONT)

time.sleep(1)
print("Terminating...")
proc.terminate()
proc.wait()

print(f"Process finished with returncode: {proc.returncode}")
