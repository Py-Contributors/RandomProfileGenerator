#!/bin/bash
if ! [ -x "$(command -v flake8)" ]; then
    echo 'Error: flake8 is not installed.' >&2
    echo 'Installing flake8...'
    pip install flake8
fi

if ! [ -x "$(command -v twine)" ]; then
    echo 'Error: twine is not installed.' >&2
    echo 'Installing twine...'
    pip install twine
fi

check_command() {
    if [ ! -x "$(command -v $1)" ]; then
        echo "$1 is not installed"
        pip install $1
        exit 1
    fi
}

# check if the git is installed
check_command git
check_command flake8
check_command twine

if ! [ -f "setup.py" ]; then
  echo 'Error: setup.py is not found.' >&2
  exit 1
fi

python3 setup.py sdist bdist_wheel

check_directory() {
    if [ ! -d "$1" ]; then
        echo "$1 is not found"
        exit 1
    fi
}

# check if the dist folder is exist
check_directory dist

python3 -m twine upload dist/*

rm -rf dist
rm -rf build
rm -rf *.egg-info
find . -name "*.pyc" -exec rm -rf {}\;
