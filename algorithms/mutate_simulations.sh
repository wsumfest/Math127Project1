OUTPUT_FILE="mutate_tests.log"
THREADS="1"
EXECUTABLE="WriteResults"

rm -f $OUTPUT_FILE

while [[ $THREADS -lt 9 ]]; do
    echo -e "Threads:$THREADS" >> $OUTPUT_FILE
    SIMULATION="1"
    while [[ $SIMULATION -lt 6 ]]; do
        ( time python -c "from test_threads_cpu import test_mutate; test_mutate($THREADS)" ) 2>> $OUTPUT_FILE
        SIMULATION=$[$SIMULATION + 1]
    done

    THREADS=$[$THREADS + 1]
done

make clean
make classes
java -cp . $EXECUTABLE $OUTPUT_FILE

