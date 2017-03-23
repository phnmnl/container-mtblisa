#!/bin/bash

fail=false

# Test on GET
run_mtblisa.py GET MTBLS2
if ! [ -e "/out.zip" ]; then
	echo "GET out.zip for MTBLS2 doesn't exist"
    fail=true
fi

# Test on GETJ
run_mtblisa.py GETJ MTBLS2
if ! [ -e "/out.json" ]; then
    echo "GETJ out.json for MTBLS2 doesn't exist"
    fail=true
fi

# Test on GET_FACTORS
run_mtblisa.py GET_FACTORS MTBLS2
if ! [ -e "/out.json" ]; then
    echo "GET_FACTORS out.json for MTBLS2 doesn't exist"
    fail=true
fi

# Test on GET_FVS
run_mtblisa.py GET_FVS MTBLS2 genotype
if ! [ -e "/out.json" ]; then
    echo "GET_FVS out.json for MTBLS2 doesn't exist"
    fail=true
fi

# Test on GET_DATA_FILES
run_mtblisa.py GET_DATA_FILES MTBLS2 "{\"genotype\": \"Col-0\"}"
if ! [ -e "/out.json" ]; then
    echo "GET_DATA_FILES out.json for MTBLS2 doesn't exist"
    fail=true
fi

if $fail ; then
    echo "Errors detected!"
    exit 1
fi

echo "All files created successfully"
