#!/bin/bash
(
  echo "Child: My PID is $$, sleeping for 2s..."
  sleep 2
  exit 7
) &

CHILD_PID=$!
echo "Parent: Spawned child with PID $CHILD_PID"

wait $CHILD_PID
EXIT_CODE=$?

echo "Parent: Child $CHILD_PID finished with exit code=$EXIT_CODE"
