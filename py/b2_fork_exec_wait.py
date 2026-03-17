import os
import sys

pid = os.fork()

if pid == 0:  # Child
    print(f"Child: I am {os.getpid()}, executing bash...")
    os.execlp("bash", "bash", "-c", "echo 'Hello from exec'; exit 7")
else:         # Parent
    child_pid, status = os.waitpid(pid, 0)
    # Коректне отримання коду завершення
    if os.WIFEXITED(status):
        exit_code = os.WEXITSTATUS(status)
        print(f"Parent: Child {child_pid} exited with code {exit_code}")
