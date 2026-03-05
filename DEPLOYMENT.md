# Deployment Guide for GitHub & Streamlit Cloud

## Quick Start: Deploy in 5 Minutes

### Step 1: Initialize Git Repository
```bash
cd "c:\Users\laura-01\Documents\AI PROJECT"
git init
git add .
git commit -m "Initial commit: Credit Risk Assessment ML Model"
```

### Step 2: Create GitHub Repository
1. Go to [github.com](https://github.com) and log in (create account if needed)
2. Click **"+"** → **"New repository"**
3. Name it: `credit-risk-assessment`
4. Add description: "ML web app for credit risk prediction"
5. Choose **Public** (so supervisor can access)
6. Click **"Create repository"**

### Step 3: Push to GitHub
```bash
git remote add origin https://github.com/YOUR-USERNAME/credit-risk-assessment.git
git branch -M main
git push -u origin main
```

### Step 4: Deploy on Streamlit Cloud (FREE & EASIEST)
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"New app"**
3. Fill in:
   - **Repository**: `YOUR-USERNAME/credit-risk-assessment`
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. Click **Deploy**
5. Wait 2-3 minutes ✨
6. Your app will have a public URL like: `https://credit-risk-assessment-xxxx.streamlit.app`

### Step 5: Share with Supervisor
Send them the Streamlit URL! They can:
- Input customer data
- See instant predictions
- View model performance metrics
- Explore feature importance

## Important Notes

⚠️ **Before deployment**, make sure you have:
- ✅ Ran `credit_risk_complete.ipynb` completely (generates `.pkl` files)
- ✅ Verified `.pkl` files are in the same folder as `app.py`
- ✅ Tested the app locally with `streamlit run app.py`

## File Structure on GitHub

Your repo should look like:
```
credit-risk-assessment/
├── app.py                              # Streamlit web app
├── credit_risk_complete.ipynb         # ML pipeline (executed)
├── application_record.csv             # Data file
├── credit_record.csv                  # Data file
├── credit_risk_best_model.pkl         # Trained model
├── credit_risk_scaler.pkl             # Feature scaler
├── credit_risk_features.pkl           # Feature list
├── credit_risk_label_encoders.pkl     # Categorical encoders
├── requirements.txt                   # Python dependencies
├── README.md                          # Project documentation
└── .gitignore                         # Files to ignore
```

## What NOT to Commit
These will be auto-ignored (in `.gitignore`):
- `venv/` or virtual environment folders
- `__pycache__/` or `.pyc` files  
- Jupyter checkpoints `.ipynb_checkpoints/`

## Troubleshooting Deployment

**"ModuleNotFoundError on Streamlit Cloud"**
- Check `requirements.txt` includes all packages
- Update it: `pip freeze > requirements.txt`

**"FileNotFoundError: Model files not found"**
- Verify `.pkl` files are committed to GitHub
- Check they're in the root directory (not in a subfolder)

**App takes too long to load**
- This is normal on first load (Streamlit Cloud takes 30-60 sec)
- Subsequent loads are faster

## Optional Enhancements

### Add a GitHub Actions CI/CD Workflow
Create `.github/workflows/test.yml`:
```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements.txt
      - run: python -m pytest  # if you add tests
```

### Custom Domain (Optional)
On Streamlit Cloud:
1. Go to app settings
2. Under "Custom domain", enter your domain
3. Follow DNS setup instructions

## Support

For issues with:
- **GitHub**: Read [GitHub Docs](https://docs.github.com)
- **Streamlit**: Check [Streamlit Docs](https://docs.streamlit.io)
- **Model/Code**: Review comments in `app.py` and notebook

---

**You're ready to go! 🚀**

Questions? Comment this guide or check Streamlit/GitHub documentation.
