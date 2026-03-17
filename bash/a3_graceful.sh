#!/bin/bash
cleanup() {
    echo -e "\nCaught signal! Performing cleanup..."
    sleep 1
    echo "Done. Exiting."
    exit 0
}

trap cleanup SIGINT SIGTERM

echo "Process PID: $$"
tick=1
while true; do
    echo "tick=$tick"
    sleep 1
    ((tick++))
done
