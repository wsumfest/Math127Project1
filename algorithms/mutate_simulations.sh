OUTPUT_FILE="mutate_tests.log"
EXECUTABLE="WriteResults"
MAC_GRAPH_OUTPUT_FILE="graphs/mac_graph_output.jpeg"
LINUX_GRAPH_OUTPUT_FILE="graphs/linux_graph_output.jpeg"

rm -f $OUTPUT_FILE
rm -rf $"../graphs"
mkdir -p "../simulations"
mkdir -p "../graphs"


run_simulation() {
    THREADS="1"
#running simulation on local machine
    while [[ $THREADS -lt 9 ]]; do
        echo -e "Threads:$THREADS" >> $OUTPUT_FILE
        SIMULATION="1"
        while [[ $SIMULATION -lt 101 ]]; do
            echo -e "Running simulation on $THREADS threads ...\n"
            ( time python -c "from test_threads_cpu import test_mutate; test_mutate($THREADS)" ) 2>> $OUTPUT_FILE
            SIMULATION=$[$SIMULATION + 1]
        done

        THREADS=$[$THREADS + 1]
    done
    make clean
    make classes
    java -cp . $EXECUTABLE $OUTPUT_FILE
}

# run_simulation
run_simulation
chmod u+x get_last_file.sh
LAST_FILE=$(./get_last_file.sh)

echo -e "Running simulation on remote server, this will take awhile.....\n"

LINUX_LAST_FILE=$(sshpass -fpassword.txt ssh cs152-be@ashby.cs.berkeley.edu "cd algorithms && ./mutate_simulations.sh && exit")

cd "../simulations"

echo -e "writing remote file to local system, this may take awhile as well....\n"

sshpass -f $"../algorithms/password.txt" scp cs152-be@ashby.cs.berkeley.edu:$"simulations/${LINUX_LAST_FILE}" $PWD

LINUX_LAST_FILE="${PWD}/${LINUX_LAST_FILE}"

cd ".."

Rscript --vanilla algorithms/make_graphs.R $LAST_FILE $MAC_GRAPH_OUTPUT_FILE
Rscript --vanilla algorithms/make_graphs.R $LINUX_LAST_FILE $LINUX_GRAPH_OUTPUT_FILE
open -a Finder $MAC_GRAPH_OUTPUT_FILE
sleep 2
open -a Finder $LINUX_GRAPH_OUTPUT_FILE

