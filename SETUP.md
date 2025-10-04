# NeuroGrid ScriptSense - Setup Guide

## Prerequisites

- Python 3.10 or higher installed ✅ (You have Python 3.10.2)

## Installation Steps

### 1. Create Virtual Environment (Optional but Recommended)

```powershell
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**If you get an execution policy error, use:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**OR use the batch file instead:**

```powershell
.\venv\Scripts\activate.bat
```

### 3. Install Required Packages

```powershell
pip install -r requirements.txt
```

### 4. Configure API Key

- Open `main.py`
- Replace the API key on line 6 with your Gradient AI Model Access Key:

```python
GRADIENT_MODEL_ACCESS_KEY = "your_actual_api_key_here"
```

**⚠️ SECURITY WARNING:** Never commit your API key to version control!

### 5. Run the Application

```powershell
streamlit run main.py
```

## Quick Start (Without Virtual Environment)

If you prefer not to use a virtual environment:

```powershell
pip install -r requirements.txt
streamlit run main.py
```

## Troubleshooting

### PowerShell Execution Policy Error

If you can't run PowerShell scripts, either:

1. Use the batch file: `.\venv\Scripts\activate.bat`
2. Change execution policy: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Package Installation Issues

Make sure pip is up to date:

```powershell
python -m pip install --upgrade pip
```

### Port Already in Use

If port 8501 is busy, specify a different port:

```powershell
streamlit run main.py --server.port 8502
```

## Dependencies

Main packages installed:

- streamlit==1.50.0 (Web framework)
- gradient>=2.0.0 (DigitalOcean Gradient AI)
- gTTS>=2.3.0 (Text-to-Speech)
- pillow (Image handling)

## Project Structure

```
Medical-Prescription-Translator/
├── main.py                          # Main application file
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── images/                          # Image assets
├── translated_prescription_Telugu.txt
└── venv/                           # Virtual environment (if created)
```

## Running the App

Once everything is installed, run:

```powershell
streamlit run main.py
```

The app will open in your default browser at `http://localhost:8501`

## Features

- Translate medical prescriptions into 27+ Indian languages
- Professional medical terminology preservation
- Download translated prescriptions as text files
- Text-to-Speech audio generation
- User-friendly interface with DigitalOcean Gradient AI

## Support

For issues, check:

1. Python version (should be 3.10+)
2. All packages installed correctly
3. API key is valid and properly configured

---

© 2025 NeuroGrid. All rights reserved.
