CURRENT_DIR='.'

get_last_saved_file (){
    FILE=$(ls -Art1 ${CURRENT_DIR} | tail -n 1)
    if [ ! -f ${FILE} ]; then
        CURRENT_DIR="${CURRENT_DIR}/${FILE}"
        get_last_saved_file
    fi
    echo $FILE
    exit
}

cd "../simulations"
get_last_saved_file