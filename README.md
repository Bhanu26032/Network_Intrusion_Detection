# Adaptive Shields for Network Intrusion Detection via Gradient Boosting

## 📌 Abstract

**Adaptive Shields for Network Intrusion Detection via Gradient Boosting** proposes an intelligent, hybrid framework to improve the performance of Network Intrusion Detection Systems (NIDS). NIDS play a crucial role in cybersecurity, enabling real-time traffic monitoring and malicious activity detection.

This research introduces a hybrid methodology combining **Hierarchical Clustering Decision Tree Twin Support Vector Machine (HC-DTTSVM)** and **Gradient Boosting Decision Trees (GBDT)**. GBDT is employed as a feature extractor to enhance the HC-DTTSVM technique’s capability to detect complex intrusion patterns. The training pipeline begins with GBDT, followed by **Artificial Neural Networks (ANN)** and **Twin Support Vector Machines (TWSVM)** to increase precision in anomaly detection.

### 🔬 Evaluation Metrics

The model is evaluated using:
- **Accuracy**
- **Precision**
- **Recall**
- **False Alarm Rate (FAR)**
- **F1-score**
- **G-Mean**

The proposed approach outperforms several baseline deep learning techniques, demonstrating its effectiveness in identifying and classifying sophisticated network intrusions.

---

## 📰 Publication Details

**Published in**: *Journal of Neonatal Surgery* (Scopus-indexed)  
**Issue**: Vol. 14 No. 16S (2025)  
**Citation**:  
Gowra B, V D. Adaptive Shields for Network Intrusion Detection via Gradient Boosting. J Neonatal Surg [Internet]. 2025 Apr 22 [cited 2025 Jun 18];14(16S):456-68.  
🔗 [Read the Article](https://www.jneonatalsurg.com/index.php/jns/article/view/4319)  
📄 [Download PDF](https://www.jneonatalsurg.com/index.php/jns/article/view/4319/3663)  

---

## 💻 Project Structure

```bash
project-root/
│
├── nslapp/                     # Django application folder
│   ├── manage.py               # Django's management utility
│   ├── settings.py             # Django settings
│   ├── urls.py                 # URL configuration
│   ├── views.py                # Web views handling
│   
│
├── ml_model/                   # Machine Learning folder
│   ├── intrusion_detection.ipynb  # Jupyter Notebook
│   ├── model.pkl               # Serialized ML model
│   └── preprocessing.py        # Custom preprocessing logic
│
├── requirements.txt            # Python dependencies
├── django.yml                  # GitHub Actions workflow file
└── README.md                   # This file


⚙️ Workflow & Steps
1️⃣ Machine Learning Model Creation
Open intrusion_detection.ipynb using Jupyter Notebook.

Perform data loading, preprocessing, and EDA.

Train a GBDT-based model (optionally include ANN and TWSVM steps).

Serialize the trained model using joblib or pickle:

python
Copy
Edit
import joblib
joblib.dump(model, 'model.pkl')
Save model.pkl inside the ml_model/ directory.

2️⃣ Django Integration
In your Django app (nslapp):

Load the trained model:

python
Copy
Edit
import joblib
import os

model_path = os.path.join(BASE_DIR, 'ml_model/model.pkl')
model = joblib.load(model_path)
Create a Django form or API to accept input traffic features.

Predict using the model:

python
Copy
Edit
def predict_intrusion(input_data):
    prediction = model.predict([input_data])
    return prediction
Display the result via the web interface.

3️⃣ GitHub Actions (CI/CD)
To ensure your project is tested on every push or pull request, GitHub Actions (django.yml) is configured to:

Set up Python environment

Install dependencies

Navigate to the Django project folder (nslapp/)

Run python manage.py test

🔍 Automatically validates code and unit tests for Python 3.7–3.9.

yaml
Copy
Edit
# django.yml
name: Django CI

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9]

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install Dependencies
      run: |
        cd nslapp
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run Tests
      run: |
        cd nslapp
        python manage.py test


🚀 How to Run
Step-by-step:
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
Create and activate a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run Django server:

bash
Copy
Edit
cd nslapp
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/.

📚 License & Open Access
This work is licensed under a Creative Commons Attribution 4.0 International License.

You are free to share, adapt, and reuse the material even for commercial use.

You must give proper credit, link to the license, and indicate if changes were made.

🔗 View License

✍️ Citation
Gowra B, V D. Adaptive Shields for Network Intrusion Detection via Gradient Boosting. J Neonatal Surg [Internet]. 2025Apr.22 [cited 2025Jun.18];14(16S):456-68.
Available from: https://www.jneonatalsurg.com/index.php/jns/article/view/4319

📧 Contact
For academic queries or collaborations:

Author: Gowra Bhanuprakash
Email: bhanu26032@gmail.com
Affiliation: Department of Computer Science & Engineering
Institution: K L University

🔍 Future Work
The proposed methodology opens several directions for future research:

Incorporating advanced ensemble learning techniques

Integrating deep learning models like RNNs/CNNs

Enhancing feature engineering for NIDS

Benchmarking across multiple real-world intrusion datasets

