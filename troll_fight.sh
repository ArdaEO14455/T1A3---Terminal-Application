#!/usr/bin/bash

source .venv/bin/activate 

python3 -m pip install

pip -V

python3 src/battle.py

deactivate

