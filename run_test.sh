#!/bin/bash

fail=false

# Test on GET
run_mtblisa.py --command GET --study MTBLS1
if ! [ -e "/out.zip" ]; then
	echo "GET out.zip for MTBLS1 doesn't exist"
    fail=true
fi

# Test on GETJ
run_mtblisa.py --command GETJ --study MTBLS1
if ! [ -e "/out.json" ]; then
    echo "GETJ out.json for MTBLS1 doesn't exist"
    fail=true
fi

# Test on GET_FACTORS
run_mtblisa.py --command GET_FACTORS --study MTBLS1
if ! [ -e "/out.json" ]; then
    echo "GET_FACTORS out.json for MTBLS1 doesn't exist"
    fail=true
fi

# Test on GET_FVS
run_mtblisa.py --command GET_FVS --study MTBLS1 --query Gender
if ! [ -e "/out.json" ]; then
    echo "GET_FVS out.json for MTBLS1 doesn't exist"
    fail=true
fi

# Test on GET_DATA_FILES
run_mtblisa.py --command GET_DATA_FILES --study MTBLS1 --query /query.json
if [ -e "/out.json" ]; then
    cat /out.json
fi

if ! [ -e "/out.json" ]; then
    echo "GET_DATA_FILES out.json for MTBLS1 doesn't exist"
    fail=true
fi

# Test on GET_SUMMARY
run_mtblisa.py --command GET_SUMMARY --study MTBLS1
if ! [ -e "/out.json" ]; then
    echo "GET_SUMMARY out.json for MTBLS1 doesn't exist"
    fail=true
fi

if $fail ; then
    echo "Errors detected!"
    exit 1
fi

echo "All files created successfully"
