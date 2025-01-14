#!/bin/bash

# Output file for results
OUTPUT_FILE="runtime_results.txt"
echo "Threads,Runtime" > $OUTPUT_FILE

# Iterate over thread counts
for THREADS in 1 2 4 8 16; do
    export OMP_NUM_THREADS=$THREADS
    echo "Running with $THREADS threads..."

    # Capture the runtime using wall clock timing
    RUNTIME=$(./mandelbrot | grep "Execution Time" | awk '{print $3}')
    echo "$THREADS,$RUNTIME" >> $OUTPUT_FILE
done

echo "Results written to $OUTPUT_FILE"
