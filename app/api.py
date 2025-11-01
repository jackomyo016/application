from fastapi import FastAPI
from fastapi import HTTPException
import numpy as np
import pandas as pd
import joblib
from typing import Optional
import mlflow


#Upload model

model_name = "production"
model_version = 1
model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}")
#API

app = FastAPI(
    title="Démonstration du modèle de prédiction de survie sur le Titanic",
    description=
    "<b>Application de prédiction de survie sur le Titanic</b> 🚢 <br>Une version par API pour faciliter la réutilisation du modèle 🚀" +\
        "<br><br><img src=\"https://media.vogue.fr/photos/5faac06d39c5194ff9752ec9/1:1/w_2404,h_2404,c_limit/076_CHL_126884.jpg\" width=\"200\">"
    )

@app.get("/")
async def show_welcome_page():
    """
    Show welcome page with model name and version.
    """

    return {
        "Message": "API de prédiction de survie sur le Titanic",
        "Model_name": 'Titanic ML',
        "Model_version": "0.4",
    }


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
