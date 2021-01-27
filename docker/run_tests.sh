#!/usr/bin/env bash

set -e

echo "Running pytest"
pytest tests --cov-report html
