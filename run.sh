#!/usr/bin/env bash

# run python scripts
#python laser.py
python stepper.py &
python inductor.py
python coinAI.py

# clean status file
> i_status.txt

