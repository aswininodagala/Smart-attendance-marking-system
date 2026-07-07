GNU nano 7.2                                                                                                                                                                          faceforge.py
# --- generate_embeddings.py ---
import os
import torch
import numpy as np
from insightface.app import FaceAnalysis
from PIL import Image
from torchvision import transforms

# ✅ Initialize InsightFace (GPU-enabled)
face_app = FaceAnalysis(name="buffalo_l", providers=['CUDAExecutionProvider'])
face_app.prepare(ctx_id=0)

# ✅ Set your dataset path
dataset_path = os.path.expanduser("~/optic-pi/student_data")

# ✅ Dict to hold embeddings
embeddings_dict = {}

# ✅ Augmentation transform
augment = transforms.Compose([
    transforms.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.4, hue=0.05),
    transforms.RandomRotation(degrees=10),
    transforms.RandomHorizontalFlip(),
    transforms.GaussianBlur(kernel_size=(3, 3)),
    transforms.RandomAffine(degrees=5, translate=(0.05, 0.05)),
])

for folder_name in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder_name)
    if not os.path.isdir(folder_path):
        continue

    roll_number = folder_name.split('_', 1)[0]
    person_key = f"{roll_number}"
    embeddings_dict[person_key] = []

    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)
        try:
            image = Image.open(img_path).convert("RGB")
            image_np = np.array(image)

            # Original Image
            faces = face_app.get(image_np)
            if len(faces) > 0:
                face = sorted(faces, key=lambda x: x.bbox[2] - x.bbox[0], reverse=True)[0]
                emb = face.normed_embedding
                embeddings_dict[person_key].append(emb)
                print(f"✅ Original: {img_name} for {person_key}")
            else:
                print(f"⛔ No face detected in original {img_name}")

            # Augmented Images
            for i in range(5):
                aug_img = augment(image)
                aug_np = np.array(aug_img)
                faces = face_app.get(aug_np)
                if len(faces) > 0:
                    face = sorted(faces, key=lambda x: x.bbox[2] - x.bbox[0], reverse=True)[0]
                    emb = face.normed_embedding
                    embeddings_dict[person_key].append(emb)
                    print(f"✅ Augmented {i+1}: {img_name} for {person_key}")
                else:
                    print(f"⛔ No face detected in aug {i+1}: {img_name}")
        except Exception as e:
            print(f"⚠ Error processing {img_path}: {e}")

# ✅ Save embeddings
torch.save(embeddings_dict, os.path.expanduser("~/optic-pi/models/student_embeddings.pt"))
print("✅ Embeddings saved to student_embeddings.pt")