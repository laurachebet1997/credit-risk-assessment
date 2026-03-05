# 💳 Credit Risk Assessment System

A machine learning web application that predicts credit risk for loan applicants using a trained Random Forest/XGBoost model.

## Project Overview

This project analyzes credit risk by combining customer application data with credit history records. It includes:
- **Data Processing**: Cleans and merges application and credit records
- **Feature Engineering**: Creates 15+ predictive features
- **Machine Learning**: Trains and tunes multiple models (Logistic Regression, Random Forest, Gradient Boosting, XGBoost)
- **Web Interface**: Interactive Streamlit app for real-time risk predictions

## Files in This Repository

- `credit_risk.ipynb` - Main Jupyter notebook with full ML pipeline
- `credit_risk_complete.ipynb` - Complete notebook (ready-to-copy version)
- `app.py` - Streamlit web application
- `application_record.csv` - Customer application data
- `credit_record.csv` - Customer credit history
- `requirements.txt` - Python dependencies
- `credit_risk_best_model.pkl` - Trained model (generated after notebook execution)
- `credit_risk_scaler.pkl` - Feature scaler (generated after notebook execution)
- `credit_risk_features.pkl` - Feature list (generated after notebook execution)
- `credit_risk_label_encoders.pkl` - Categorical encoders (generated after notebook execution)

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd AI\ PROJECT
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Generate Model Artifacts
First, run the Jupyter notebook to train the model and generate `.pkl` files:
```bash
jupyter notebook credit_risk_complete.ipynb
```
- Execute all cells in the notebook
- This will train the model and save the necessary `.pkl` files

### 5. Run the Web App Locally
```bash
streamlit run app.py
```
The app will open in your browser at `http://localhost:8501`

## How to Use the Web App

1. **Make Prediction Tab**: Enter customer information and click "Assess Credit Risk"
   - Personal information (age, gender, marital status)
   - Financial information (income, assets)
   - Employment & education details
   - Credit history metrics

2. **Model Info Tab**: View model architecture, performance metrics, and features used

3. **Feature Importance Tab**: See which features most influence risk predictions

## Model Performance

| Metric | Score |
|--------|-------|
| ROC-AUC | ~0.75 |
| Accuracy | ~70% |
| Precision | High |
| Recall | Balanced |

## Deployment Options

### Option A: Deploy on Streamlit Cloud (Free & Easiest)
1. Push repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app" → Select your GitHub repo, branch, and `app.py`
4. Streamlit will automatically deploy and provide a public URL

### Option B: Deploy on GitHub Pages + GitHub Actions
1. Create a GitHub Actions workflow to build and host
2. Use a custom domain if desired

### Option C: Deploy on Heroku/AWS/Azure
1. Install Heroku CLI
2. Create `Procfile`: `web: streamlit run --logger.level=error app.py`
3. Deploy: `heroku create` and `git push heroku main`

## Key Features

✅ Real-time credit risk predictions  
✅ Interactive web interface  
✅ Model performance metrics & feature importance  
✅ Easy deployment for supervisors to review  
✅ Comprehensive ML pipeline with hyperparameter tuning  

## Data Description

### Features Used (15 engineered features)
- Income-related: Annual income, income per family member
- Employment: Years employed, employment category
- Demographic: Age, family size, gender, marital status
- Assets: Owns car, owns property, has contact channels
- Credit History: Account age, default status, average monthly risk, account history length
- Risk Indicators: High-risk credit history, limited work history

### Target Variable
- **HAS_DEFAULTED**: 1 = Bad payer/Defaulted, 0 = Good payer/On-time payments

## Dependencies

See `requirements.txt` for all dependencies. Key packages:
- **streamlit** - Web framework
- **scikit-learn** - ML models and preprocessing
- **xgboost** - Gradient boosting
- **pandas** - Data manipulation
- **joblib** - Model serialization

## Troubleshooting

**"ModuleNotFoundError: No module named 'xgboost'"**
```bash
pip install xgboost
```

**"FileNotFoundError: Model files not found"**
- Ensure you ran the Jupyter notebook completely
- Check that `.pkl` files are in the same directory as `app.py`

**App won't start**
```bash
pip install -r requirements.txt --upgrade
```

## Next Steps

1. Run the notebook to generate model artifacts
2. Test the app locally with `streamlit run app.py`
3. Push to GitHub
4. Deploy on Streamlit Cloud
5. Share the URL with your supervisor!

## Contact & Support

For questions or improvements, please reach out or create an issue in the repository.

---

**Last Updated**: March 2026  
**Model Version**: 1.0 (Tuned Random Forest/XGBoost)
