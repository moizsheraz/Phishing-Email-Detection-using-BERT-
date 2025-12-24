# 🚀 Quick Deployment Steps

## Deploy to Hugging Face Spaces in 5 Minutes

### 1. Create Space
- Go to: https://huggingface.co/new-space
- Name: `phishing-email-detection`
- SDK: **Gradio**
- Click "Create"

### 2. Upload Files
Upload these 3 files:
- ✅ `app.py`
- ✅ `requirements.txt`
- ✅ `README.md`

### 3. Wait for Build
- Takes 2-5 minutes
- Watch build logs
- Done! 🎉

### 4. Your Space URL
```
https://huggingface.co/spaces/YOUR-USERNAME/phishing-email-detection
```

## Required Files Checklist

- [x] `app.py` - Gradio interface (provided)
- [x] `requirements.txt` - Dependencies (provided)
- [x] `README.md` - With YAML metadata (provided)
- [ ] Model at `moizsheraz/phishing-detection-model` (ensure it's uploaded)

## Model Upload (If Needed)

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load your trained model
model = AutoModelForSequenceClassification.from_pretrained("./your_model_path")
tokenizer = AutoTokenizer.from_pretrained("./your_model_path")

# Upload to Hugging Face
model.push_to_hub("moizsheraz/phishing-detection-model")
tokenizer.push_to_hub("moizsheraz/phishing-detection-model")
```

## Testing Your Deployment

Try these test cases:

**Phishing:**
```
URGENT: Your account will be closed! 
Click: http://fake-bank.com
```

**Legitimate:**
```
Hi Team, Meeting at 2 PM Tuesday.
```

## Need Help?

- 📖 See `DEPLOYMENT_GUIDE.md` for detailed instructions
- 🐛 Check build logs if deployment fails
- 💬 Visit https://discuss.huggingface.co/ for support

---
**That's it!** Your demo will be live in minutes. 🚀
