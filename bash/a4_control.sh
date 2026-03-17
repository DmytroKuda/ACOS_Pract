#!/bin/bash
sleep 100 &
PID=$!
echo "Started sleep 100 with PID: $PID"

echo "Sending SIGSTOP..."
kill -STOP $PID
ps -p $PID -o pid,stat,comm

sleep 1
echo "Sending SIGCONT..."
kill -CONT $PID
ps -p $PID -o pid,stat,comm

sleep 1
echo "Terminating process..."
kill -TERM $PID
echo "Process $PID terminated."
