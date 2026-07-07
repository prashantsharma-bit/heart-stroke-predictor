Heart Stroke Risk Prediction Dashboard
https://img.shields.io/badge/python-3.9+-blue.svg
https://img.shields.io/badge/Streamlit-1.39.0-FF4B4B.svg
https://img.shields.io/badge/License-MIT-yellow.svg

A machine learning web application that predicts the risk of heart stroke based on patient medical data. Built with Streamlit and Logistic Regression, this tool provides an interactive dashboard for healthcare professionals and researchers.

📋 Table of Contents
Overview

Demo

Features

Dataset

Model Performance

Tech Stack

Installation

Usage

Model Training

Project Structure

Ethical Considerations

Future Improvements

Contributing

License

🎯 Overview
This project leverages the Framingham Heart Study dataset to predict whether a patient is at high risk of a heart stroke. It implements a Logistic Regression model with preprocessing pipeline and serves predictions via a user-friendly Streamlit dashboard.

Key Prediction Factors:

Age (strongest predictor)

Systolic Blood Pressure

BMI

Smoking Status

Diabetes & Hypertension History

🚀 Demo
https://via.placeholder.com/800x400?text=Heart+Stroke+Risk+Dashboard

Try it live: (Deploy your own using Streamlit Cloud)

✨ Features
🔍 Prediction Capabilities
Input 14 medical parameters including vital signs, lifestyle factors, and blood work

Real-time risk assessment with probability scores

Color-coded results (🔴 High Risk / 🟢 Low Risk)

📊 Model Insights
Feature importance visualization (coefficient analysis)

Debug mode to inspect scaled inputs and model parameters

Educational sidebar explaining top risk factors

🛠️ Technical Features
Pre-trained Logistic Regression model with joblib serialization

Min-Max scaling for feature normalization

Cached model loading for faster performance

📊 Dataset
Source: Framingham Heart Study (cleaned version)
Size: 4,238 patient records, 15 features + target

Feature	Description	Type
Gender	Male/Female	Categorical
age	Age in years	Continuous
currentSmoker	Smoking status	Binary
cigsPerDay	Cigarettes smoked per day	Discrete
BPMeds	Blood pressure medication	Binary
prevalentStroke	History of stroke	Binary
prevalentHyp	History of hypertension	Binary
diabetes	Diabetes status	Binary
totChol	Total cholesterol (mg/dL)	Continuous
sysBP	Systolic blood pressure (mm Hg)	Continuous
diaBP	Diastolic blood pressure (mm Hg)	Continuous
BMI	Body Mass Index	Continuous
heartRate	Heart rate (bpm)	Discrete
glucose	Glucose level (mg/dL)	Continuous
Heart_ stroke	Target: Stroke diagnosis	Binary (No/Yes)
📈 Model Performance
Logistic Regression (Current Model)
Metric	Value
Accuracy	85.7%
ROC-AUC	0.71
Precision (Stroke)	0.60
Recall (Stroke)	0.07
Random Forest (Comparison)
Metric	Value
Accuracy	84.9%
Precision (Stroke)	0.41
Recall (Stroke)	0.07
⚠️ Note: Both models suffer from class imbalance — stroke cases represent only ~10% of the dataset, leading to low recall. Future improvements should focus on oversampling (SMOTE) or threshold tuning.

🛠️ Tech Stack
Frontend: Streamlit

Modeling: Scikit-learn

Data Processing: Pandas, NumPy

Visualization: Matplotlib

Serialization: Joblib

💻 Installation
1. Clone the Repository
bash
git clone https://github.com/yourusername/heart-stroke-predictor.git
cd heart-stroke-predictor
2. Set Up Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
pip install -r requirements.txt
requirements.txt:

text
streamlit==1.39.0
joblib==1.4.2
numpy==1.26.4
pandas==2.2.2
matplotlib==3.8.4
scikit-learn==1.4.1.post1
🖥️ Usage
Run the Streamlit App
bash
streamlit run app.py
Interactive Input
Fill in patient details using sliders and dropdowns

Click "Predict Heart Stroke Risk"

View results:

Risk level (High/Low)

Probability percentage

Health recommendations

Debug Mode (Sidebar)
Expand "Debug Info" to inspect scaled input values

View model coefficients and intercept

🧠 Model Training
The model was trained in model.ipynb with the following steps:

Data Preprocessing
Handled missing values with median imputation

Encoded categorical variables (Gender, prevalentStroke, Heart_ stroke)

Dropped education column (not significant)

Applied Min-Max Scaling to normalize features

Model Selection
Logistic Regression (baseline)

Random Forest (comparison)

Evaluation Metrics
Accuracy, Precision, Recall, F1-Score

ROC-AUC

Confusion Matrix

Feature Importance Analysis

Save Artifacts
python
joblib.dump(model, 'heart_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
📁 Project Structure
text
heart-stroke-predictor/
│
├── app.py                      # Streamlit dashboard
├── heart_model.pkl             # Trained Logistic Regression model
├── scaler.pkl                  # MinMaxScaler parameters
├── clean_heart_disease.csv     # Cleaned dataset
├── heart_disease.csv           # Original dataset (before cleaning)
├── model.ipynb                 # Jupyter notebook for training
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore
⚖️ Ethical Considerations
Patient Privacy
Data Anonymization: The dataset contains no PII (Name, Address, Contact Info)

Purpose Limitation: For educational and research use only — not for clinical decision-making

Security: Real-world deployment would require HIPAA/GDPR compliance, encryption, and access controls

Bias Mitigation
Fairness: Future work must include stratified analysis across age, gender, and ethnic groups

Transparency: Model limitations (low recall) are clearly communicated

🔮 Future Improvements
✅ Class Balancing: Apply SMOTE to handle stroke class imbalance

✅ Threshold Tuning: Optimize decision threshold for better recall

✅ Advanced Models: Test XGBoost, Neural Networks

✅ Feature Engineering: Add interactions (e.g., BMI × Age)

✅ Deployment: Package with Docker for cloud deployment

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a feature branch: git checkout -b feature/amazing-feature

Commit changes: git commit -m 'Add amazing feature'

Push to branch: git push origin feature/amazing-feature

Open a Pull Request

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

👨‍💻 Author
Your Name
https://img.shields.io/badge/GitHub-YourGitHub-181717?logo=github
https://img.shields.io/badge/LinkedIn-YourLinkedIn-0A66C2?logo=linkedin
📧 your.email@example.com

🙏 Acknowledgments
Framingham Heart Study for providing the dataset

Scikit-learn and Streamlit communities for excellent open-source tools

Healthcare professionals for their invaluable domain insights

📌 Quick Links
Streamlit Documentation

Scikit-learn Logistic Regression

Framingham Heart Study

⭐ Star this repository if you found it useful!

