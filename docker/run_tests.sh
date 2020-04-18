#!/usr/bin/env bash

set -e

ACTIVATE_PYENV="true"
BLACK_ACTION="--check"
ISORT_ACTION="--check-only"

function usage
{
    echo "usage: run_tests.sh [--format-code]"
    echo ""
    echo " --format-code : Format the code instead of checking formatting"
    exit 1
}

echo "${$#}"
# while [[ $# -gt 0 ]]; do
#     arg="$1"
#     echo "${arg}"
#     # case $arg in
#     #     --format-code)
#     #     BLACK_ACTION="--quiet"
#     #     ISORT_ACTION="-y"
#     #     ;;
#     #     --no-pyenv)
#     #     ACTIVATE_PYENV="false"
#     #     ;;
#     #     -h|--help)
#     #     usage
#     #     ;;
#     #     "")
#     #     # ignore
#     #     ;;
#     #     *)
#     #     echo "Unexpected argument: ${arg}"
#     #     usage
#     #     ;;
#     # esac
# done
echo "done"

if [[ "${ACTIVATE_PYENV}" = "true" ]]; then
    eval "$(pyenv init -)"
    pyenv activate app
fi

echo "Done2"

# echo "Running iSort..."
# isort -rc ${ISORT_ACTION} .

# echo "Running black..."
# black ${BLACK_ACTION} app tests

# echo "Running flake8"
# flake8 .

# pytest tests --cov-report html