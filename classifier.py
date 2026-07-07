import torch
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score  # <-- Add this
import os

# Load .pt embeddings
embedding_path = os.path.expanduser("~/optic-pi/models/student_embeddings.pt")
data = torch.load(embedding_path, weights_only=False)

X = []
y = []

for person_id, embeddings in data.items():
    for emb in embeddings:
        X.append(emb)
        y.append(person_id)

X = np.array(X)
y = np.array(y)

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Train SVM
svm_model = SVC(kernel='linear', probability=True)
svm_model.fit(X, y_encoded)

# ✅ Calculate and show training accuracy
y_pred = svm_model.predict(X)
accuracy = accuracy_score(y_encoded, y_pred)
print(f"✅ SVM Training Accuracy: {accuracy * 100:.2f}%")

# Save model and encoder
model_save_path = os.path.expanduser("~/optic-pi/models/svm_model.pt")
torch.save({'model': svm_model, 'encoder': label_encoder}, model_save_path)
print("✅ SVM model and label encoder saved.")