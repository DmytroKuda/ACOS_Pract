#!/bin/bash
echo "My PID: $$"
echo "My PPID: $PPID"
echo "Process info from ps:"
ps -p $$ -o pid,ppid,stat,ni,comm
