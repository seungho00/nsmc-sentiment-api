from fastapi import FastAPI
from pydantic import BaseModel

from backend.predict import tokenize, predict


app = FastAPI()


class SentimentRequest(BaseModel):
    sentence: str


@app.post("/predict")
def predict_sentiment(request: SentimentRequest):
    encoding = tokenize(request.sentence)
    negative, positive = predict(encoding)

    return {
        "sentence": request.sentence,
        "negative": negative,
        "positive": positive
    }