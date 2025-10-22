#!/bin/bash

echo "Lancement de l'application"
python3 train.py

echo "Lancement de l'API"
uvicorn app.api:app --host "0.0.0.0" --reload
