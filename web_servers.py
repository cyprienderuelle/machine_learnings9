import fastapi
import joblib as jl

app = fastapi.FastAPI()

@app.get("/predict")
def read_root():
    return {"y_pred": 2}

app.post("/predict")
def predict(size: float, nb_rooms: int, garden: bool):
    model = jl.load("regression.joblib")

    prediction = model.predict([[size, nb_rooms, garden]])
    return {"y_pred": prediction[0]}

