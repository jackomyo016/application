#!/bin/bash
echo "Lancement de l'API"
uvicorn app.api:app --host "0.0.0.0" --reload
