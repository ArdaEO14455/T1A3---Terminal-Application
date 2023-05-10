#!/usr/bin/bash -x

If ($IsWindows)
If ($IsLinux)
If ($IsMacOS)

source .venv/bin/activate

# python3 -m pip install --upgrade pip
# pip3 install -U pytest
pip -V

python3 main.py

