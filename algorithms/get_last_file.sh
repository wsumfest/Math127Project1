CURRENT_DIR='.'

get_last_saved_file (){
    FILE=$(ls -Art1 ${CURRENT_DIR} | tail -n 1)
    if [ ! -f ${FILE} ]; then
        CURRENT_DIR="${CURRENT_DIR}/${FILE}"
        get_last_saved_file
    fi
    FILE_WITH_EXTENSION="${PWD}/${FILE}"
    echo $FILE_WITH_EXTENSION
    exit
}

cd "../simulations"
get_last_saved_file