from fastapi import FastAPI
from fastapi import HTTPException
import numpy as np
import pandas as pd
import joblib
from typing import Optional


app = FastAPI()
model = joblib.load("model.joblib")

@app.get("/")
async def root():
    return "API pour prédire grâce au modèle Titanic"


@app.get("/prediction")
async def predict(
    Pclass: int,
    Name: str,
    Sex: str,
    SibSp: int,
    Parch: int,
    Ticket: str,
    Fare: float,
    Age: Optional[float] = None,
    Cabin: Optional[str] = None,
    Embarked: Optional[str] = None,
) -> str:

    Age = Age if Age is not None else np.nan
    Cabin = Cabin if Cabin is not None else np.nan
    Embarked = Embarked if Embarked is not None else np.nan

    sample = pd.DataFrame(
        [[
            np.int64(Pclass),
            Name,
            Sex,
            Age,
            SibSp,
            Parch,
            Ticket,
            Fare,
            Cabin,
            Embarked
        ]],
        columns=['Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare','Cabin', 'Embarked']
    )

    prediction = model.predict(sample)
    return f"Prédiction : {int(prediction[0])}"
