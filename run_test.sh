#!/bin/bash

fail=false

# Test on GET
python3 run_mtblisa.py GET MTBLS2
if ! [ -e "/out.zip" ]; then
	echo "GET out.zip for MTBLS2 doesn't exist"
    fail=true
fi

# Test on GETJ
python3 run_mtblisa.py GETJ MTBLS2
if ! [ -e "/out.json" ]; then
    echo "GETJ out.json for MTBLS2 doesn't exist"
    fail=true
fi

# Test on GET_FACTORS
python3 run_mtblisa.py GETJ MTBLS2
if ! [ -e "/out.json" ]; then
    echo "GET_FACTORS out.json for MTBLS2 doesn't exist"
    fail=true
fi

# Test on GET_FVS
python3 run_mtblisa.py GETJ MTBLS2 genotype
if ! [ -e "/out.json" ]; then
    echo "GET_FVS out.json for MTBLS2 doesn't exist"
    fail=true
fi

# Test on GET_DATA_FILES
python3 run_mtblisa.py GETJ MTBLS2 "{\"genotype\": \"Col-0\"}"
if ! [ -e "/out.json" ]; then
    echo "GET_DATA_FILES out.json for MTBLS2 doesn't exist"
    fail=true
fi

if $fail ; then
    echo "Errors detected!"
    exit 1
fi

echo "All files created successfully"
