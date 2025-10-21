#!/bin/bash

python3 train.py
uvicorn app.api:api --host "0.0.0.0" --reload &
