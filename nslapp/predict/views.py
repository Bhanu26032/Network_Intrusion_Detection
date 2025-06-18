import numpy as np
import joblib
from django.shortcuts import render
from sklearn.preprocessing import LabelEncoder

# Load the trained model
new_model = joblib.load('NSL.pkl')

# Define attack types
attack_labels = ['normal', 'neptune', 'warezclient', 'ipsweep', 'portsweep', 'teardrop', 'nmap',
                 'satan', 'smurf', 'pod', 'guess_passwd', 'back', 'ftp_write', 'multihop',
                 'rootkit', 'buffer_overflow', 'imap', 'warezmaster', 'phf', 'land',
                 'loadmodule', 'spy', 'perl']

# Initialize label encoder
label_encoder = LabelEncoder()
label_encoder.fit(attack_labels)

def predict_attack(request):
    context = {
        "feature_range": range(1, 18),
        "attack_type": None,  # Initialize with None
        "features": {f"feature{i}": "" for i in range(1, 18)}  # Empty features initially
    }
    
    if request.method == "POST":
        try:
            features = []
            for i in range(1, 18):
                feature_name = f"feature{i}"
                value = request.POST.get(feature_name)
                if value is None or value.strip() == "":
                    raise ValueError(f"Missing input for {feature_name}")
                features.append(float(value))
                context["features"][feature_name] = value  # Store the entered value

            # Convert inputs to numpy array for prediction
            example_input = np.array([features])
            prediction = new_model.predict(example_input)
            attack_type = label_encoder.inverse_transform(prediction)[0]

            context.update({
                "attack_type": attack_type,
                "color": "green" if attack_type == "normal" else "red"
            })

        except Exception as e:
            context["error"] = str(e)

    return render(request, "predict/predict.html", context) 