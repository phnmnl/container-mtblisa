#!/bin/bash


my_path="$(readlink -f "${0}")"
my_dir="$(dirname "${my_path}")"


function log() {
    echo "${@}" >&2
}

set -x

have_failures=false

"${my_dir}/run_tests.py" || have_failures=true

# check correctly reported parsing errors
isaslicer.py get-my-error ${TestStudy} out --format zip
exit_code=$?
if [[ $exit_code = 0 ]]; then
    log "Failed to report bad subcommand name"
    have_failures=true
fi

isaslicer.py mtbls-get-study IDontExist out
exit_code=$?
if [[ $exit_code = 0 ]]; then
    log "Failed to report bad study id"
    have_failures=true
fi

isaslicer.py mtbls-get-study
exit_code=$?
if [[ $exit_code = 0 ]]; then
    log "Failed to report bad usage"
    have_failures=true
fi

if [[ $have_failures = true ]]; then
    log "Errors detected!"
    exit 1
else
    log "All files created successfully"
fi