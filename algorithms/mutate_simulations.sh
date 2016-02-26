OUTPUT_FILE="mutate_tests.log"
THREADS="1"

rm -f $OUTPUT_FILE

while [[ $THREADS -lt 5 ]]; do
    echo -e "Running 5 simulations on $THREADS threads ..." >> $OUTPUT_FILE
    SIMULATION="1"
    while [[ $SIMULATION -lt 6 ]]; do
        echo -e "Simulation: $SIMULATION:" >> $OUTPUT_FILE
        ( time python -c "from test_threads_cpu import test_mutate; test_mutate($THREADS)" ) 2>> $OUTPUT_FILE
        SIMULATION=$[$SIMULATION + 1]
    done

    THREADS=$[$THREADS + 1]
done


