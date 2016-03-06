OUTPUT_FILE="mutate_tests.log"
THREADS="1"
EXECUTABLE="WriteResults"
GRAPH_OUTPUT_FILE="graphs/graph_output.jpeg"

rm -f $OUTPUT_FILE
mkdir -p "../simulations"
mkdir -p "../graphs"

while [[ $THREADS -lt 9 ]]; do
    echo -e "Threads:$THREADS" >> $OUTPUT_FILE
    SIMULATION="1"
    while [[ $SIMULATION -lt 51 ]]; do
        echo -e "Running simulation on $THREADS threads ...\n"
        ( time python -c "from test_threads_cpu import test_mutate; test_mutate($THREADS)" ) 2>> $OUTPUT_FILE
        SIMULATION=$[$SIMULATION + 1]
    done

    THREADS=$[$THREADS + 1]
done

make clean
make classes
java -cp . $EXECUTABLE $OUTPUT_FILE
chmod u+x get_last_file.sh
LAST_FILE=$(./get_last_file.sh)
cd ".."
rm -f $GRAPH_OUTPUT_FILE
Rscript --vanilla algorithms/make_graphs.R $LAST_FILE $GRAPH_OUTPUT_FILE
open -a Finder $GRAPH_OUTPUT_FILE
