# 🚀 Quick Reference: Gradient AI Migration

## ⚡ Quick Commands

### Install Dependencies

```powershell
pip install -r requirements.txt
```

### Run Application

```powershell
streamlit run main.py
```

### Verify Setup

```powershell
python check_env.py
```

---

## 🔑 API Key Setup

1. Get key: https://cloud.digitalocean.com/account/api/tokens
2. Open: `main.py` (line 6)
3. Replace: `"your_gradient_model_access_key_here"`

---

## 📝 Key Changes Made

| Component | Before (Gemini)              | After (Gradient AI)             |
| --------- | ---------------------------- | ------------------------------- |
| SDK       | `google-generativeai`        | `gradient`                      |
| Import    | `import google.generativeai` | `from gradient import Gradient` |
| API Key   | `GEMINI_API_KEY`             | `GRADIENT_MODEL_ACCESS_KEY`     |
| Model     | `gemini-pro`                 | `llama3.3-70b-instruct`         |
| Function  | `gemini_pro_response()`      | `gradient_ai_response()`        |

---

## 🎯 Testing Steps

1. ✅ Get API key from DigitalOcean
2. ✅ Update `main.py` line 6
3. ✅ Run `python check_env.py`
4. ✅ Run `streamlit run main.py`
5. ✅ Test with sample prescription
6. ✅ Verify translation quality

---

## 🔧 Available Models

Change in `main.py` (around line 22):

```python
model="llama3.3-70b-instruct",  # Recommended (best quality)
model="llama3.1-70b-instruct",  # Alternative
model="llama3.1-8b-instruct",   # Faster, smaller
model="mixtral-8x7b-instruct",  # Alternative
```

---

## 📚 Documentation Files

- `GRADIENT_AI_SETUP.md` - Complete setup guide
- `MIGRATION_GUIDE.md` - Detailed migration steps
- `README.md` - Project overview
- `QUICK_START.md` - Quick start guide

---

## ⚠️ Common Issues

### Issue: "Invalid API Key"

**Fix:** Use Model Access Key, not API token

### Issue: "Module not found: gradient"

**Fix:** `pip install gradient`

### Issue: API connection errors

**Fix:** Verify your Gradient API key is correct in `main.py`

---

## 💡 Pro Tips

1. **Use .env file** for API key (more secure)
2. **Try different models** for best results
3. **Monitor usage** in DigitalOcean console
4. **Never commit** API keys to Git

---

## 📞 Support Resources

- Gradient Docs: https://gradientai-sdk.digitalocean.com/
- DigitalOcean Console: https://cloud.digitalocean.com/
- API Tokens: https://cloud.digitalocean.com/account/api/tokens

---

**Ready to go?** Just add your API key and run: `streamlit run main.py`
