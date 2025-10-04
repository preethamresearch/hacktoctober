# Migration from Gemini AI to DigitalOcean Gradient AI

## Overview

The NeuroGrid ScriptSense has been migrated from Google Gemini AI to **DigitalOcean Gradient AI**. This guide explains the changes and how to set up the new version.

---

## What Changed?

### 1. **SDK Replacement**

- **Old:** Google Generative AI (`google-generativeai`)
- **New:** DigitalOcean Gradient AI (`gradient`)

### 2. **API Key**

- **Old:** `GEMINI_API_KEY`
- **New:** `GRADIENT_MODEL_ACCESS_KEY`

### 3. **Model**

- **Old:** `gemini-pro`
- **New:** `llama3.3-70b-instruct` (Llama 3.3 70B Instruct)

### 4. **API Interface**

- **Old:** `genai.GenerativeModel().generate_content()`
- **New:** `gradient.chat.completions.create()` (OpenAI-compatible interface)

---

## Getting Your Gradient AI API Key

### Step 1: Create a DigitalOcean Account

1. Go to [DigitalOcean](https://www.digitalocean.com/)
2. Sign up for an account (if you don't have one)

### Step 2: Generate Model Access Key

1. Log in to [DigitalOcean Console](https://cloud.digitalocean.com/)
2. Navigate to the **API** section
3. Click on **Tokens/Keys** tab
4. Click **Generate New Token** or **Model Access Key**
5. Copy your **Model Access Key**

**Note:** For serverless inference, you need a **Model Access Key**, not just an API token.

---

## Installation

### Uninstall Old Dependencies

```powershell
pip uninstall google-generativeai google-ai-generativelanguage google-api-python-client google-auth google-auth-httplib2 -y
```

### Install New Dependencies

```powershell
pip install -r requirements.txt
```

Or install just the Gradient SDK:

```powershell
pip install gradient
```

---

## Configuration

### Update API Key in main.py

**Line 6-8 in main.py:**

**Old:**

```python
GEMINI_API_KEY = "AIzaSyBkIxH9VqRQJp9lvhKKbLs8bUj28u-dP0M"
genai.configure(api_key=GEMINI_API_KEY)
```

**New:**

```python
GRADIENT_MODEL_ACCESS_KEY = "your_gradient_model_access_key_here"
gradient_client = Gradient(model_access_key=GRADIENT_MODEL_ACCESS_KEY)
```

### Replace with Your Key

Open `main.py` and replace `"your_gradient_model_access_key_here"` with your actual Gradient Model Access Key.

---

## Code Changes Summary

### Import Changes

```python
# Old
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

# New
from gradient import Gradient
```

### Function Changes

```python
# Old
def gemini_pro_response(text, target_language):
    gemini_pro_model = genai.GenerativeModel("gemini-pro")
    response = gemini_pro_model.generate_content(prompt)
    return response.text

# New
def gradient_ai_response(text, target_language):
    response = gradient_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3.3-70b-instruct",
    )
    return response.choices[0].message.content
```

---

## Available Models

Gradient AI provides access to various models:

- **llama3.3-70b-instruct** (Default - Best for general tasks)
- **llama3.1-70b-instruct**
- **llama3.1-8b-instruct**
- **mixtral-8x7b-instruct**
- And more...

To use a different model, change the `model` parameter in `main.py`:

```python
model="llama3.1-70b-instruct",  # or any other available model
```

---

## Benefits of Gradient AI

### 1. **Better Performance**

- Llama 3.3 70B is a powerful open-source model
- Fast inference times with serverless deployment

### 2. **Cost-Effective**

- Competitive pricing compared to proprietary models
- Pay-per-use model

### 3. **Privacy & Control**

- DigitalOcean infrastructure
- More control over data processing

### 4. **OpenAI-Compatible API**

- Familiar interface for developers
- Easy migration from OpenAI-based apps

---

## Testing the Migration

### 1. Verify Environment

```powershell
python check_env.py
```

Expected output:

```
✅ streamlit                 - Installed
✅ gradient                  - Installed
✅ pandas                    - Installed
✅ numpy                     - Installed
✅ PIL                       - Installed
✅ requests                  - Installed
```

### 2. Run the Application

```powershell
streamlit run main.py
```

### 3. Test Translation

1. Fill in patient details
2. Add a medication
3. Select a target language (e.g., Hindi)
4. Click "Translate"
5. Verify the translation is accurate

---

## Troubleshooting

### Error: "Invalid API Key"

- Verify your Gradient Model Access Key is correct
- Make sure you're using a **Model Access Key**, not a regular API token
- Check that the key is properly set in `main.py`

### Error: "Module 'gradient' not found"

```powershell
pip install gradient
```

### Old Google packages still installed

```powershell
pip uninstall google-generativeai -y
pip install -r requirements.txt
```

### Translation quality issues

- The Llama 3.3 70B model may translate differently than Gemini
- You can adjust the prompt in the `gradient_ai_response()` function
- Try different models available on Gradient AI

---

## Reverting to Gemini (If Needed)

If you need to revert to Gemini AI:

1. Restore the old `main.py` from git:

   ```powershell
   git checkout HEAD~1 main.py
   ```

2. Reinstall Gemini dependencies:
   ```powershell
   pip install google-generativeai
   ```

---

## Environment Variable Approach (Recommended)

For better security, use environment variables:

### 1. Install python-dotenv

```powershell
pip install python-dotenv
```

### 2. Create .env file

```env
GRADIENT_MODEL_ACCESS_KEY=your_actual_key_here
```

### 3. Update main.py

```python
from dotenv import load_dotenv
import os

load_dotenv()
GRADIENT_MODEL_ACCESS_KEY = os.getenv("GRADIENT_MODEL_ACCESS_KEY")
gradient_client = Gradient(model_access_key=GRADIENT_MODEL_ACCESS_KEY)
```

---

## Next Steps

1. ✅ Get your Gradient AI Model Access Key
2. ✅ Update the API key in `main.py`
3. ✅ Install dependencies: `pip install -r requirements.txt`
4. ✅ Run verification: `python check_env.py`
5. ✅ Test the app: `streamlit run main.py`

---

## Resources

- [Gradient AI Documentation](https://gradientai-sdk.digitalocean.com/)
- [Serverless Inference Guide](https://gradientai-sdk.digitalocean.com/getting-started/serverless-inference/)
- [DigitalOcean Console](https://cloud.digitalocean.com/)
- [Model Access Keys](https://cloud.digitalocean.com/account/api/tokens)

---

## Support

For issues or questions:

1. Check the [Gradient AI Documentation](https://gradientai-sdk.digitalocean.com/)
2. Verify your API key is correct
3. Run `python check_env.py` to check your environment

---

**Migration Complete! 🚀**

Your NeuroGrid ScriptSense is now powered by DigitalOcean Gradient AI.

---

_Last Updated: October 4, 2025_
