from django.shortcuts import render
import joblib
import os
import numpy as np

# Absolute path to the model components
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'readmission_model.pkl')
model = joblib.load(MODEL_PATH)

def predict_readmission(request):
    # 1. If the user clicked the button (POST request)
    if request.method == 'POST':
        try:
            # Extract values from form text inputs
            age = float(request.POST.get('age', 62))
            time_in_hospital = float(request.POST.get('time_in_hospital', 5))
            num_lab_procedures = float(request.POST.get('num_lab_procedures', 42))
            num_medications = float(request.POST.get('num_medications', 14))
            number_diagnoses = float(request.POST.get('number_diagnoses', 4))
            primary_diagnosis = float(request.POST.get('primary_diagnosis', 0))

            # Shape data array for Scikit-Learn pipeline framework
            input_features = np.array([[age, time_in_hospital, num_lab_procedures, 
                                        num_medications, number_diagnoses, primary_diagnosis]])
            
            # Compute operational inferences
            prediction = model.predict(input_features)[0]
            probabilities = model.predict_proba(input_features)[0]
            prob_percent = probabilities[1] * 100

            result_status = "High" if prediction == 1 else "Low"

            # Create the exact data packets the Chart.js visual dashboard needs
            context = {
                'prediction_text': f"Classification Result: {result_status} Risk of Readmission",
                'probability': round(prob_percent, 1),
                'inputs': {
                    'age': int(age),
                    'time_in_hospital': int(time_in_hospital),
                    'num_lab_procedures': int(num_lab_procedures),
                    'num_medications': int(num_medications),
                    'number_diagnoses': int(number_diagnoses),
                    'primary_diagnosis': str(int(primary_diagnosis))
                }
            }
            return render(request, 'prediction_app/index.html', context)

        except Exception as e:
            # Catch errors gracefully if something goes wrong
            return render(request, 'prediction_app/index.html', {'prediction_text': f"Execution Error: {str(e)}"})

    # 2. If they are just opening the page for the first time (GET request)
    return render(request, 'prediction_app/index.html')