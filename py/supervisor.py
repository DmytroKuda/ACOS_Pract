import subprocess
import time
import sys

MAX_RESTARTS = 3
restart_count = 0

while restart_count < MAX_RESTARTS:
    print(f"\n--- Supervisor: Starting worker (Attempt {restart_count + 1}) ---")
    process = subprocess.Popen([sys.executable, "py/worker.py"])
    
    try:
        process.wait()
    except KeyboardInterrupt:
        print("\nSupervisor received Ctrl+C, terminating worker...")
        process.terminate()
        process.wait()
        break

    print(f"Supervisor: Worker exited with code {process.returncode}")
    restart_count += 1
    time.sleep(1)

print("Supervisor: Max restarts reached or stopped.")
