#!/bin/sh

black --line-length=100 autoboot/
isort --profile=black autoboot/
flake8 --max-line-length=100 autoboot/
