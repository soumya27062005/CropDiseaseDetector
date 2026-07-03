import numpy as np
import json
from tensorflow.keras.models import load_model
from PIL import Image
from tensorflow.keras.preprocessing import image
import numpy as np

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(256, 256))
    img_array = image.img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)  # Shape: (1, 256, 256, 3)



'''def preprocess_image(image_path):
    image = Image.open(image_path).resize((224, 224))
    image = np.array(image) / 255.0
    return image.reshape(1, 224, 224, 3)'''

def load_treatments(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)

def predict_and_suggest(model_path, labels, treatment_file, image_path):
    model = load_model(model_path, compile=False)
    image = preprocess_image(image_path)
    prediction = model.predict(image)
    predicted_index = np.argmax(prediction)
    disease = labels[predicted_index]
    treatments = load_treatments(treatment_file)

    print("\n✅ Detected Disease:", disease)
    if disease in treatments:
        print("🧪 Spray:", treatments[disease]["spray"])
        print("💧 Dosage:", treatments[disease]["dosage"])
        print("⏱️ Interval:", treatments[disease]["interval"])
    else:
        print("❗ No treatment data available for this disease.")




def corn(image_path):
    labels = ["Corn___Common_Rust", "Corn___Gray_Leaf_Spot", "Corn___Northern_Leaf_Blight", "Corn___Healthy"]
    predict_and_suggest("corn.h5", labels, "corn_treatments.json", image_path)

def potato(image_path):
    labels = ["Potato___Early_Blight", "Potato___Late_Blight", "Potato___Healthy"]
    predict_and_suggest("potato.h5", labels, "potato_treatments.json", image_path)

def rice(image_path):
    labels = ["Rice___Brown_Spot", "Rice___Leaf_Blast", "Rice___Neck_Blast", "Rice___Healthy"]
    predict_and_suggest("rice.h5", labels, "rice_treatments.json", image_path)

def wheat(image_path):
    labels = ["Wheat___Brown_Rust", "Wheat___Yellow_Rust", "Wheat___Healthy"]
    predict_and_suggest("wheat.h5", labels, "wheat_treatments.json", image_path)

def sugarcane(image_path):
    labels = ["Sugarcane___Red_Rot", "Sugarcane___Bacterial_Blight", "Sugarcane___Healthy"]
    predict_and_suggest("sugarcane.h5", labels, "sugarcane_treatments.json", image_path)


print("🌾 Select your crop:")
print("1. Corn")
print("2. Potato")
print("3. Rice")
print("4. Wheat")
print("5. Sugarcane")

choice = input("Enter 1–5: ")
image_path = input("Enter image file path: ")

if choice == "1":
    corn(image_path)
elif choice == "2":
    potato(image_path)
elif choice == "3":
    rice(image_path)
elif choice == "4":
    wheat(image_path)
elif choice == "5":
    sugarcane(image_path)
else:
    print("❌ Invalid selection.")
