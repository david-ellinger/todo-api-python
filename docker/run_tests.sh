#!/usr/bin/env bash

set -e

function usage
{
    echo "usage: run_tests.sh"
    exit 1
}


echo "Running pytest"
pytest tests --cov-report html
