import fastapi
import joblib as jl
from pydantic import BaseModel

app = fastapi.FastAPI()

class Item(BaseModel):
    size: int
    nb_rooms: int
    garden: bool

@app.get("/predict")
def read_root():
    return {"y_pred": 2}

@app.post("/predict")
def predict(item: Item):
    model = jl.load("regression.joblib")

    prediction = model.predict([[item.size, item.nb_rooms, item.garden]])
    return {"y_pred": prediction[0]}

