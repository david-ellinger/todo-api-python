#!/usr/bin/env bash

set -e

# echo "Running iSort..."
# isort -rc .

# echo "Running black..."
# black app tests

echo "Running flake8"
flake8 .

# echo "Running bandit"
# bandit -r app
