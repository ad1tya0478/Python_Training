import librosa
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)

    # MFCC
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_feat = [
        np.mean(mfcc),
        np.std(mfcc),
        np.var(mfcc),
        np.mean(np.diff(mfcc))
    ]

    # ZCR
    zcr = librosa.feature.zero_crossing_rate(y)
    zcr_feat = [np.mean(zcr), np.std(zcr)]

    # Spectral Centroid
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    centroid_feat = [np.mean(centroid), np.std(centroid)]

    # RMS
    rms = librosa.feature.rms(y=y)
    rms_feat = [np.mean(rms), np.std(rms)]

    # Pitch (pYIN)
    f0, voiced_flag, _ = librosa.pyin(
        y, fmin=50, fmax=300, sr=sr
    )
    pitch = f0[voiced_flag]

    if len(pitch) > 0:
        pitch_feat = [np.mean(pitch), np.std(pitch), np.var(pitch)]
    else:
        pitch_feat = [0, 0, 0]

    return mfcc_feat + zcr_feat + centroid_feat + rms_feat + pitch_feat


# Build dataset (X, y)
# Example file lists
ai_files = [
    "sample voice1.mp3"
]

human_files = [
    "my_voice.mp3",
    "my_voice2.mp3"
]

X = []
y = []

# AI voices → label = 1
for file in ai_files:
    X.append(extract_features(file))
    y.append(1)

# Human voices → label = 0
for file in human_files:
    X.append(extract_features(file))
    y.append(0)

X = np.array(X)
y = np.array(y)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# How prediction works (single file)
feat = extract_features("test_voice.wav")
feat = scaler.transform([feat])

prediction = model.predict(feat)
prob = model.predict_proba(feat)

print("Prediction:", "AI" if prediction[0] == 1 else "Human")
print("Confidence:", prob)