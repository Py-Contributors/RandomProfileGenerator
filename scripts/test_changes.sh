#!/bin/sh

# function to check the command exist or not
check_command() {
    if [ ! -x "$(command -v $1)" ]; then
        echo "$1 is not installed"
        pip install $1
        exit 1
    fi
}

# check if the git is installed
check_command git
check_command pytest
check_command flake8

# run flask8 and pytest

flake8 
pytest -e 

# check the exit code of the last command
if [ $? -eq 0 ]; then
    echo "All tests passed"
else
    echo "Some tests failed"
    exit 1
fi

