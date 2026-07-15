# 🛠 INSTALLATION & SETUP GUIDE

A complete step-by-step guide to get the Crop Disease Detection system up and running on your machine.

---

## 📦 Requirements

- Python 3.10 or 3.11
- pip (Python package manager)
- Git
- (Optional) virtualenv or venv

---

## 🚀 Step 1: Clone the Repository


git clone https://github.com/soumya27062005/cropdiseasedetector.git
cd cropdiseasedetector

## Set Up a Virtual Environment (Recommended)
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate 
---



## 📥 Step 3: Install Dependencies
pip install tensorflow numpy pillow fastapi uvicorn


You can also use:
pip install -r requirements.txt


If you include a requirements.txt file later.
---

## 🧠 Step 4: Download .h5 Model Files
Place these models inside the models/ folder of the project.
---



 ## 🔔 Rename each file as needed (potato.h5, wheat.h5, etc.) and place them in the models/ directory.
 ---


## 🧾 Step 5: Add Treatment Recommendation Files
Create a treatments/ folder and add one .json file per crop. Example for potato:
{
  "Potato___Early_blight": "Spray with Mancozeb 75% WP @ 2.5 g/litre",
  "Potato___Late_blight": "Use Metalaxyl + Mancozeb 64% WP @ 2.5 g/litre",
  "Potato___Healthy": "No treatment needed!"
}
---


Repeat similarly for each crop class based on model predictions.

## 🧪 Step 6: Run Detection Script
Example command:
python detect.py --crop potato --image images/test_leaf.jpg

---
Expected Output:
🦠 Disease: Potato___Early_blight  
✅ Confidence: 94.6%  
💊 Recommended Treatment: Spray with Mancozeb 75% WP @ 2.5 g/litre




## ⚙️ Optional: FastAPI Integration (for API Use)
Install FastAPI and dependencies:
pip install fastapi uvicorn python-multipart


Run the API server (if app included):
uvicorn app.main:app --reload


Then open your browser at:
http://127.0.0.1:8000/docs


Use Swagger UI to upload images and test predictions.
---
## ✅ You're All Set!
Now your system is ready to detect crop diseases and recommend treatments with deep learning. You can now improve the model, expand the dataset, or deploy it as a mobile/web solution!

Let me know when you’re ready to generate a matching `requirements.txt` or share it on GitHub—I’d love to see how it turns out!

---
