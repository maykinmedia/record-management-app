#!/bin/bash

set -ex

toplevel=$(git rev-parse --show-toplevel)

cd $toplevel

# Base (& prod) deps
pip-compile \
    --no-emit-index-url \
    --upgrade \
    requirements/base.in

# Dependencies for testing
pip-compile \
    --no-emit-index-url \
    --upgrade \
    --output-file requirements/ci.txt \
    requirements/base.txt \
    requirements/test-tools.in

# Dev depedencies - exact same set as CI + some extra tooling
pip-compile \
    --no-emit-index-url \
    --upgrade \
    --output-file requirements/dev.txt \
    requirements/ci.txt \
    requirements/dev.in
