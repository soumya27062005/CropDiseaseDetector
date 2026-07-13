
# 🌿 Crop Disease Detection

A machine learning project that identifies plant diseases from leaf images of crops such as **Potato, Rice, Wheat, Corn, and Sugarcane**, and returns treatment recommendations.

---

## 🚀 Features

- 🧠 Uses pre-trained `.h5` models for image classification  
- 🖼️ Accepts real crop leaf images as input  
- 💊 Suggests treatments based on detected disease  
- 🔗 Ready for integration with FastAPI or other web services  

---

## 🛠 Tech Stack

- Python 3.10+
- TensorFlow / Keras
- NumPy, Pillow
- JSON for treatment data
- (Optional) FastAPI for API deployment

---


---

## 🖼️ How It Works

1. Load the correct `.h5` model based on crop type  
2. Preprocess the input image (resize, normalize)  
3. Predict disease class using the model  
4. Fetch treatment advice from a `.json` file  
5. Display result with disease name and solution  

 

