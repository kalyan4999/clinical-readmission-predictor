# 🏥 Clinical Readmission Risk Portal
### End-to-End Predictive Decision Support Engine

A full-stack clinical data analytics application that integrates a trained Machine Learning pipeline with a responsive web dashboard to predict patient 30-day readmission risk. Built using **Django**, **Scikit-Learn**, and **Chart.js**.

---

## 📊 Live Dashboard Preview

<div align="center">
  <img src="prediction_app/[Screenshot 2026-06-01 232022.png](https://github.com/kalyan4999/clinical-readmission-predictor/blob/main/prediction_app/Screenshot%202026-06-02%20234334.png)" alt="Clinical Portal Dashboard" width="800">
</div>

---

## 💡 Core Features
* **Real-Time ML Inference:** Processes patient demographics and clinical metrics through an optimized `RandomForestClassifier` pipeline.
* **Dynamic Data Visualizations:** Utilizes **Chart.js** to render real-time probabilistic risk gauges and baseline patient-vs-hospital deviation bar charts.
* **Clinical Metrics Auditing:** Evaluates parameters like hospital stay duration, comorbidity diagnoses, and lab complexity proxies to assist in point-of-care discharge planning.

## 🛠️ Tech Stack
* **Backend Framework:** Django (Python)
* **Machine Learning:** Scikit-Learn, Numpy, Joblib
* **Frontend UI:** Bootstrap 5, HTML5, CSS3
* **Data Visualization:** Chart.js (JavaScript)
* **Database:** SQLite
