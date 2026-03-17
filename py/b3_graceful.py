import signal
import time
import os

stop = False

def handler(signum, frame):
    global stop
    print(f"\nReceived signal {signum}")
    stop = True

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

print(f"Running... PID: {os.getpid()}")
tick = 1
while not stop:
    print(f"tick={tick}")
    time.sleep(1)
    tick += 1

print("Performing cleanup...")
time.sleep(1)
print("Finished.")
