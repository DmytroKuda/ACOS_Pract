import signal
import time
import os

def handler(signum, frame):
    print(f"Worker {os.getpid()} received signal, shutting down...")
    exit(0)

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

print(f"Worker started (PID: {os.getpid()})")
while True:
    print(f"Worker {os.getpid()} is working...")
    time.sleep(2)
