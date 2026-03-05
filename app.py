import streamlit as st
import pandas as pd
import numpy as np
import joblib
import warnings
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(page_title="Credit Risk Assessment", layout="wide")

# Load model and preprocessing objects
@st.cache_resource
def load_model_artifacts():
    try:
        model = joblib.load('credit_risk_best_model.pkl')
        scaler = joblib.load('credit_risk_scaler.pkl')
        features = joblib.load('credit_risk_features.pkl')
        label_encoders = joblib.load('credit_risk_label_encoders.pkl')
        return model, scaler, features, label_encoders
    except FileNotFoundError:
        st.error("Model files not found. Please run the notebook first to generate the model artifacts.")
        return None, None, None, None

model, scaler, features, label_encoders = load_model_artifacts()

# Page title and description
st.title("💳 Credit Risk Assessment System")
st.markdown("---")
st.write("This app predicts whether a customer is at risk of defaulting on credit payments based on their application and credit history.")

if model is None:
    st.stop()

# Create tabs for different sections
tab1, tab2, tab3 = st.tabs(["📊 Make Prediction", "ℹ️ Model Info", "📈 Feature Importance"])

with tab1:
    st.subheader("Enter Customer Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Personal Information**")
        gender = st.selectbox("Gender", ["M", "F"])
        age = st.slider("Age", 18, 80, 35)
        marital_status = st.selectbox("Marital Status", ["Civil marriage", "Married", "Separated", "Single / not married", "Widow"])
        family_size = st.slider("Family Size", 1, 10, 2)
        children_count = st.number_input("Number of Children", 0, 10, 0)
    
    with col2:
        st.write("**Financial Information**")
        annual_income = st.number_input("Annual Income ($)", 0, 1000000, 50000)
        owns_car = st.selectbox("Owns Car", ["Y", "N"])
        owns_property = st.selectbox("Owns Property", ["Y", "N"])
        phone = st.checkbox("Has Phone")
        email = st.checkbox("Has Email")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.write("**Employment & Education**")
        income_category = st.selectbox("Income Category", 
                                       ["Working", "Commercial associate", "Pensioner", "State servant", "Student"])
        employment_years = st.slider("Employment Years", 0, 40, 5)
        occupation = st.selectbox("Occupation", 
                                  ["Accountants", "Cleaning staff", "Cooking staff", "Core staff", "Drivers", 
                                   "HR staff", "High skill tech staff", "IT staff", "Laborers", 
                                   "Low-skill Laborers", "Managers", "Medicine staff", "Private service staff", 
                                   "Realty agents", "Sales staff", "Secretaries", "Security staff", "Unknown", 
                                   "Waiters/barmen staff"])
        education_level = st.selectbox("Education Level",
                                       ["Secondary / secondary special", "Higher education", 
                                        "Incomplete higher", "Lower secondary", "Academic degree"])
    
    with col4:
        st.write("**Credit History**")
        total_months_tracked = st.slider("Total Months Credit History", 0, 120, 24)
        average_monthly_risk = st.slider("Average Monthly Risk (0-1)", 0.0, 1.0, 0.1, step=0.05)
        account_age_months = st.slider("Account Age (Months)", 0, 120, 24)
    
    st.markdown("---")
    
    # Prepare data for prediction
    if st.button("🔍 Assess Credit Risk", type="primary"):
        try:
            # Create input dataframe
            input_data = pd.DataFrame({
                'GENDER': [gender],
                'OWNS_CAR': [owns_car],
                'OWNS_PROPERTY': [owns_property],
                'ANNUAL_INCOME': [annual_income],
                'INCOME_CATEGORY': [income_category],
                'EDUCATION_LEVEL': [education_level],
                'MARITAL_STATUS': [marital_status],
                'PHONE': [int(phone)],
                'EMAIL': [int(email)],
                'AGE': [age],
                'EMPLOYEMENT_YEARS': [employment_years],
                'OCCUPATION': [occupation],
                'FAMILY_SIZE': [family_size],
                'CHILDREN_COUNT': [children_count],
                'TOTAL_MONTHS_TRACKED': [total_months_tracked],
                'AVERAGE_MONTHLY_RISK': [average_monthly_risk],
                'ACCOUNT_AGE_MONTHS': [account_age_months]
            })
            
            # Feature Engineering: Create the same engineered features as in training
            input_data['IS_UNEMPLOYED'] = (input_data['EMPLOYEMENT_YEARS'] < 0).astype(int)
            input_data['HAS_LIMITED_WORK_HISTORY'] = (input_data['EMPLOYEMENT_YEARS'] < 1).astype(int)
            input_data['OWNS_ASSETS'] = ((input_data['OWNS_CAR'] == 'Y') | (input_data['OWNS_PROPERTY'] == 'Y')).astype(int)
            input_data['HIGH_RISK_CREDIT_HISTORY'] = (input_data['AVERAGE_MONTHLY_RISK'] > 0.3).astype(int)
            input_data['LONG_ACCOUNT_HISTORY'] = (input_data['ACCOUNT_AGE_MONTHS'] > 24).astype(int)
            
            # Encode categorical variables
            input_encoded = input_data.copy()
            for col in label_encoders.keys():
                if col in input_encoded.columns:
                    input_encoded[col] = label_encoders[col].transform(input_encoded[col].astype(str))
            
            # Select only features used in training
            X_input = input_encoded[features].fillna(0)
            
            # Scale ALL features (since the scaler was trained on encoded data)
            X_input_scaled = X_input.copy()
            X_input_scaled[features] = scaler.transform(X_input[features])
            
            # Make prediction
            prediction = model.predict(X_input_scaled)[0]
            prediction_proba = model.predict_proba(X_input_scaled)[0]
            
            # Display results
            st.markdown("---")
            st.subheader("📋 Assessment Results")
            
            col_result1, col_result2 = st.columns(2)
            
            with col_result1:
                if prediction == 0:
                    st.success("✅ **LOW RISK** - Customer is likely to pay on time")
                    risk_level = "Low"
                    confidence = prediction_proba[0]
                else:
                    st.error("⚠️ **HIGH RISK** - Customer may default on payments")
                    risk_level = "High"
                    confidence = prediction_proba[1]
            
            with col_result2:
                st.metric("Risk Confidence Score", f"{confidence*100:.2f}%")
            
            # Risk breakdown
            st.write("**Risk Score Breakdown:**")
            col_prob1, col_prob2 = st.columns(2)
            with col_prob1:
                st.write(f"Good Payer Probability: {prediction_proba[0]*100:.2f}%")
            with col_prob2:
                st.write(f"Default Risk Probability: {prediction_proba[1]*100:.2f}%")
            
            # Visualization
            st.progress(confidence, text=f"{risk_level} Risk: {confidence*100:.1f}%")
            
        except Exception as e:
            st.error(f"Error during prediction: {str(e)}")

with tab2:
    st.subheader("Model Information")
    
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        st.write("**Model Type:** Tuned Random Forest / XGBoost Classifier")
        st.write("**Training Data:** 30,000+ customer records")
        st.write("**Target Variable:** Default Status (Good Payer vs. Defaulter)")
    
    with col_info2:
        st.write("**ROC-AUC Score:** ~0.75")
        st.write("**Accuracy:** ~70%")
        st.write("**Features Used:** 15 engineered features")
    
    st.markdown("---")
    st.write("**Features Used in Model:**")
    features_display = pd.DataFrame({'Features': features})
    st.dataframe(features_display, use_container_width=True)

with tab3:
    st.subheader("Top Features by Importance")
    
    try:
        # Get feature importance from model
        if hasattr(model, 'feature_importances_'):
            importances = model.feature_importances_
            feature_importance_df = pd.DataFrame({
                'Feature': features,
                'Importance': importances
            }).sort_values('Importance', ascending=False).head(10)
            
            st.bar_chart(feature_importance_df.set_index('Feature')['Importance'], use_container_width=True)
            
            st.write("**Top 10 Most Important Features:**")
            st.dataframe(feature_importance_df, use_container_width=True)
        else:
            st.info("Feature importance data not available for this model type")
    except Exception as e:
        st.info(f"Unable to display feature importance: {str(e)}")

# Footer
st.markdown("---")
st.markdown("*Credit Risk Assessment System | ML Model Deployment | © 2026*")
