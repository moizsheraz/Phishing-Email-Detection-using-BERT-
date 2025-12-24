# 🚀 Hugging Face Spaces Deployment Guide

This guide will walk you through deploying the PhishGuard AI application to Hugging Face Spaces.

## Prerequisites

- A Hugging Face account (free): [Sign up here](https://huggingface.co/join)
- Your trained BERT model uploaded to Hugging Face Model Hub at `moizsheraz/phishing-detection-model`
- Basic understanding of Git (optional, for Git-based deployment)

## Deployment Method 1: Web Interface (Easiest)

### Step 1: Create a New Space

1. Go to [huggingface.co/new-space](https://huggingface.co/new-space)
2. Fill in the details:
   - **Space name**: `phishing-email-detection` (or your preferred name)
   - **License**: MIT
   - **Select SDK**: Choose **Gradio**
   - **Hardware**: CPU (Basic) - Free tier is sufficient
   - **Visibility**: Public (recommended for demo) or Private

3. Click **Create Space**

### Step 2: Upload Files

After creating the Space, you'll be on the Space page. Click on **Files** tab:

1. Upload the following files from this repository:
   - `app.py` - The Gradio application
   - `requirements.txt` - Python dependencies
   - `README.md` - Project documentation (includes Spaces metadata)

2. You can drag and drop files or use the "Add file" button

### Step 3: Wait for Build

- Hugging Face Spaces will automatically detect the files and start building
- You'll see a build log showing the progress
- The build typically takes 2-5 minutes
- Once complete, your app will be live!

### Step 4: Access Your Space

Your app will be available at:
```
https://huggingface.co/spaces/YOUR-USERNAME/phishing-email-detection
```

## Deployment Method 2: Git (Advanced)

### Step 1: Create Space via Web

Follow Step 1 from Method 1 to create an empty Space.

### Step 2: Clone the Space Repository

```bash
# Clone your Space
git clone https://huggingface.co/spaces/YOUR-USERNAME/phishing-email-detection
cd phishing-email-detection
```

### Step 3: Add Your Files

```bash
# Copy files from this repository
cp /path/to/this/repo/app.py .
cp /path/to/this/repo/requirements.txt .
cp /path/to/this/repo/README.md .
```

### Step 4: Commit and Push

```bash
# Add files
git add .

# Commit
git commit -m "Initial deployment of PhishGuard AI"

# Push to Hugging Face
git push
```

### Step 5: Wait for Deployment

The Space will automatically build and deploy after you push.

## Deployment Method 3: Using Hugging Face CLI

### Step 1: Install Hugging Face CLI

```bash
pip install huggingface_hub
```

### Step 2: Login to Hugging Face

```bash
huggingface-cli login
```

Enter your Hugging Face token when prompted (get it from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens))

### Step 3: Create and Upload Space

```bash
# From this repository's root directory
huggingface-cli upload-space . YOUR-USERNAME/phishing-email-detection --repo-type space
```

## Verifying Your Model

Before deploying, ensure your model is properly uploaded to Hugging Face Model Hub:

1. Go to [huggingface.co/YOUR-USERNAME/phishing-detection-model](https://huggingface.co/moizsheraz/phishing-detection-model)
2. Verify these files are present:
   - `config.json`
   - `pytorch_model.bin` or `model.safetensors`
   - `tokenizer_config.json`
   - `vocab.txt`
   - `special_tokens_map.json`

If your model is not yet uploaded, you can upload it:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load your local model
model = AutoModelForSequenceClassification.from_pretrained("./path/to/your/model")
tokenizer = AutoTokenizer.from_pretrained("./path/to/your/model")

# Push to Hugging Face Hub
model.push_to_hub("moizsheraz/phishing-detection-model")
tokenizer.push_to_hub("moizsheraz/phishing-detection-model")
```

## Configuration Options

### Custom Model Path

If your model is at a different location, update `app.py`:

```python
HF_REPO = "your-username/your-model-name"
```

### Environment Variables

You can set environment variables in your Space settings:

1. Go to your Space settings
2. Click on "Variables and secrets"
3. Add variables like:
   - `HF_TOKEN` - For private models
   - `MODEL_PATH` - Alternative model path

### Custom Hardware

If you need GPU acceleration:

1. Go to Space settings
2. Under "Hardware", select a GPU option (requires payment)
3. Recommended for larger models or high traffic

## Troubleshooting

### Build Failed

**Issue**: Space shows build error

**Solutions**:
- Check the build logs for specific errors
- Ensure `requirements.txt` has all necessary dependencies
- Verify Python syntax in `app.py`
- Make sure README.md has proper YAML frontmatter

### Model Not Loading

**Issue**: "Model not loaded" error

**Solutions**:
- Verify model exists at `moizsheraz/phishing-detection-model`
- Check if model is private (may need HF_TOKEN)
- Ensure model format is compatible with `transformers` library
- Check Spaces logs for specific error messages

### App Crashes

**Issue**: Space shows runtime error

**Solutions**:
- Check the Logs tab in your Space
- Verify all imports are in `requirements.txt`
- Test locally first: `python app.py`
- Check for memory issues (upgrade hardware if needed)

### Slow Loading

**Issue**: App takes long to start

**Solutions**:
- This is normal for first load (model downloading)
- Consider using a smaller model
- Upgrade to GPU hardware for faster inference
- Use model caching features

## Testing Your Deployment

Once deployed, test with these example emails:

### Test 1: Phishing Email
```
URGENT: Your account has been compromised!
Click here immediately to verify: http://fake-bank.com
```

### Test 2: Legitimate Email
```
Hi Team,
Meeting scheduled for Tuesday at 2 PM.
See you then!
```

### Test 3: Suspicious Email
```
You've won $1,000,000! Send your bank details to claim.
```

## Updating Your Space

To update your deployed Space:

**Via Web**:
1. Go to your Space
2. Click "Files"
3. Edit or upload new files
4. Space will auto-rebuild

**Via Git**:
```bash
# Make changes locally
git add .
git commit -m "Update app"
git push
```

## Monitoring and Analytics

### View Usage Stats

1. Go to your Space page
2. Check the "Analytics" tab for:
   - Number of visitors
   - API calls
   - Usage over time

### Check Logs

1. Click "Logs" tab in your Space
2. View real-time application logs
3. Monitor for errors or issues

## Best Practices

1. **Test Locally First**: Always test `app.py` locally before deploying
2. **Version Control**: Keep your Space in sync with your GitHub repo
3. **Documentation**: Keep README.md updated with usage instructions
4. **Model Updates**: Document model version and update date
5. **Error Handling**: Ensure graceful error messages for users
6. **Rate Limiting**: Consider adding rate limiting for public Spaces
7. **Privacy**: Don't log or store user inputs if dealing with real emails

## Additional Resources

- [Gradio Documentation](https://gradio.app/docs/)
- [Hugging Face Spaces Documentation](https://huggingface.co/docs/hub/spaces)
- [Transformers Library Docs](https://huggingface.co/docs/transformers/)
- [Hugging Face Hub Python Library](https://huggingface.co/docs/huggingface_hub/)

## Support

If you encounter issues:

1. Check the [Hugging Face Forums](https://discuss.huggingface.co/)
2. Review [Gradio Discord](https://discord.gg/gradio)
3. Open an issue on this GitHub repository
4. Check Hugging Face Spaces status page

## Example Spaces

Check out similar deployed Spaces for reference:
- [Text Classification Demos](https://huggingface.co/spaces?sort=likes&search=text-classification)
- [BERT-based Applications](https://huggingface.co/spaces?sort=likes&search=bert)

---

**Ready to Deploy?** Follow Method 1 above to get started! 🚀
