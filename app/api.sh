#!/bin/bash

source venv/bin/activate
python train.py
uvicorn app.api:app --host 0.0.0.0 --reload &
