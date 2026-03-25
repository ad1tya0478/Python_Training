from fastapi import FastAPI, UploadFile, File
import joblib
import tempfile
import os

from abhi_ml import extract_features

app = FastAPI()

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


@app.post("/predict")
async def predict_audio(file: UploadFile = File(...)):
    """
    1. Receive audio file from user
    2. Save temporarily
    3. Extract features
    4. Scale features
    5. Predict using trained model
    6. Return result
    """

    # Ensure correct file type (basic safety)
    if not file.filename.endswith((".wav", ".mp3", ".m4a")):
        return {"error": "Unsupported file format"}

    temp_path = None

    try:
        # 1️⃣ Save uploaded audio to a temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
            temp.write(await file.read())
            temp_path = temp.name

        # 2️⃣ Feature extraction (ML guy’s responsibility)
        features = extract_features(temp_path)
        # features shape: (n_features,)

        # 3️⃣ Scale features (same scaler used during training)
        features_scaled = scaler.transform([features])
        # shape becomes: (1, n_features)

        # 4️⃣ Prediction
        prediction = model.predict(features_scaled)[0]
        confidence = model.predict_proba(features_scaled).max()

        # 5️⃣ Clean temp file
        os.remove(temp_path)

        # 6️⃣ Return response
        return {
            "prediction": "AI Voice" if prediction == 1 else "Human Voice",
            "confidence": round(confidence * 100, 2)
        }

    except Exception as e:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)
        return {"error": str(e)}

