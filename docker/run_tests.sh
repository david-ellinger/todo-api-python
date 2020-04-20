#!/usr/bin/env bash

set -e

BLACK_ACTION="--check"
ISORT_ACTION="--check-only"

function usage
{
    echo "usage: run_tests.sh [--format-code]"
    echo ""
    echo " --format-code : Format the code instead of checking formatting"
    exit 1
}

for arg in "$@"
do
    if [ "$arg" == "--format-code" ]
    then
        BLACK_ACTION="--quiet"
        ISORT_ACTION="-y"
    elif [ "$arg" == "--help" || "$arg" == "-h" ]
    then
        usage
    fi
done
# while [[ $# -gt 0 ]]; do
#     echo $arg

    # case $arg in
    #     --format-code)
    #     BLACK_ACTION="--quiet"
    #     ISORT_ACTION="-y"
    #     shift
    #     ;;
    #     -h|--help)
    #     usage
    #     ;;
    #     "")
    #     # ignore
    #     ;;
    #     *)
    #     echo "Unexpected argument: ${arg}"
    #     usage
    #     ;;
    # esac
# done


echo "Running iSort..."
isort -rc ${ISORT_ACTION} .

echo "Running black..."
black ${BLACK_ACTION} app tests

echo "Running flake8"
flake8 .

pytest tests --cov-report html