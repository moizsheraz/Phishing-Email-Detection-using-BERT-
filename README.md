---
title: PhishGuard AI - Phishing Email Detection
emoji: 🛡️
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
license: mit
---

# 🛡️ PhishGuard AI - Phishing Email Detection

A modern web application for detecting phishing emails using BERT (Bidirectional Encoder Representations from Transformers). Deployed on Hugging Face Spaces with an interactive Gradio interface.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c.svg)
![BERT](https://img.shields.io/badge/BERT-Transformers-yellow.svg)
![Gradio](https://img.shields.io/badge/Gradio-4.0-orange.svg)

## 📁 Project Structure

```
phishing_detector/
├── app.py                 # Flask application
├── app_fastapi.py         # FastAPI application  
├── requirements.txt       # Flask dependencies
├── requirements_fastapi.txt # FastAPI dependencies
├── final_model/           # Your trained BERT model (place here)
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   └── vocab.txt
├── templates/
│   └── index.html         # Frontend template
└── static/
    ├── css/
    │   └── style.css      # Cybersecurity-themed styles
    └── js/
        └── app.js         # Frontend JavaScript
```

## 🚀 Quick Start

### Live Demo on Hugging Face Spaces

Try the live demo: [PhishGuard AI on Hugging Face Spaces](https://huggingface.co/spaces/moizsheraz/phishing-email-detection)

### Local Installation

#### Option 1: Gradio Interface (Recommended for Demo)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Gradio app
python app.py
```

Visit: `http://localhost:7860`

#### Option 2: Flask (Original Implementation)

First, rename `main.py` to use it:

```bash
# Install Flask dependencies
pip install flask flask-cors torch transformers

# Run the Flask application
python main.py
```

Visit: `http://localhost:5000`

#### Option 3: FastAPI (For Production)

```bash
# Install dependencies
pip install -r requirements_fastapi.txt

# Run the application
python app_fastapi.py

# Or with uvicorn directly
uvicorn app_fastapi:app --host 0.0.0.0 --port 8000 --reload
```

Visit: `http://localhost:8000`

FastAPI also provides:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔧 Configuration

### Using Your Trained Model

Place your trained model files in the `final_model/` directory:

```bash
mkdir final_model
# Copy your model files:
# - config.json
# - model.safetensors (or pytorch_model.bin)
# - tokenizer.json
# - vocab.txt
# - special_tokens_map.json
# - tokenizer_config.json
```

Or set the model path via environment variable:

```bash
export MODEL_PATH=/path/to/your/model
python app.py
```

### If You Don't Have a Trained Model

The application will automatically download and use `bert-base-uncased` as a fallback. This won't give accurate phishing predictions but allows you to test the UI and API.

## 📡 API Endpoints

### Health Check
```http
GET /api/health
```

Response:
```json
{
    "status": "healthy",
    "model_loaded": true
}
```

### Single Email Prediction
```http
POST /api/predict
Content-Type: application/json

{
    "text": "Dear customer, your account has been compromised..."
}
```

Response:
```json
{
    "prediction": "Phishing",
    "is_phishing": true,
    "confidence": 94.32,
    "probabilities": {
        "legitimate": 5.68,
        "phishing": 94.32
    }
}
```

### Batch Prediction
```http
POST /api/batch_predict
Content-Type: application/json

{
    "emails": [
        "First email content...",
        "Second email content..."
    ]
}
```

Response:
```json
{
    "results": [
        {"index": 0, "prediction": "Legitimate", ...},
        {"index": 1, "prediction": "Phishing", ...}
    ],
    "summary": {
        "total": 2,
        "phishing": 1,
        "legitimate": 1
    }
}
```

## 🚀 Deploy to Hugging Face Spaces

### Step-by-Step Deployment

1. **Create a Hugging Face Account**: Sign up at [huggingface.co](https://huggingface.co/)

2. **Create a New Space**:
   - Go to [huggingface.co/new-space](https://huggingface.co/new-space)
   - Choose a name for your Space (e.g., "phishing-email-detection")
   - Select "Gradio" as the SDK
   - Choose visibility (Public or Private)

3. **Upload Files**:
   - Upload `app.py` (Gradio interface)
   - Upload `requirements.txt` (dependencies)
   - Upload `README.md` (with YAML frontmatter)

4. **Automatic Deployment**:
   - Hugging Face Spaces will automatically build and deploy your app
   - Wait for the build to complete (usually 2-5 minutes)
   - Your app will be live at `https://huggingface.co/spaces/YOUR-USERNAME/SPACE-NAME`

### Alternative: Deploy via Git

```bash
# Clone your Space repository
git clone https://huggingface.co/spaces/YOUR-USERNAME/SPACE-NAME
cd SPACE-NAME

# Copy the files
cp /path/to/app.py .
cp /path/to/requirements.txt .
cp /path/to/README.md .

# Commit and push
git add .
git commit -m "Initial deployment"
git push
```

### Environment Variables (Optional)

If you need to configure environment variables:
1. Go to your Space settings
2. Add variables under "Repository secrets"
3. Common variables: `MODEL_PATH`, `HF_TOKEN`, etc.

## 🐳 Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# For Flask
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

# For FastAPI (uncomment below, comment above)
# CMD ["uvicorn", "app_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t phishguard .
docker run -p 5000:5000 phishguard
```

## 🎨 Features

### Gradio Interface
- **Interactive Demo**: Easy-to-use web interface powered by Gradio
- **Real-time Analysis**: Instant phishing detection with confidence scores
- **Example Emails**: Pre-loaded examples for quick testing
- **Rich Output**: Formatted results with visual indicators and security tips
- **Responsive Design**: Works on desktop and mobile devices

### Original Flask/FastAPI Interface
- **Batch Processing**: Analyze multiple emails at once (Flask version)
- **Modern UI**: Dark cybersecurity theme with glassmorphism effects
- **Visual Feedback**: Animated confidence meters and status indicators
- **REST API**: Programmatic access via API endpoints

## 📊 Model Details

The model is based on BERT (`bert-base-uncased`) fine-tuned for binary classification:
- **Input**: Email text (lowercased, max 512 tokens)
- **Output**: Legitimate (0) or Phishing (1)
- **Architecture**: 12-layer transformer with classification head

## 🔐 Production Considerations

1. **HTTPS**: Use a reverse proxy (nginx) with SSL certificates
2. **Rate Limiting**: Implement request throttling
3. **Authentication**: Add API key or OAuth for protected endpoints
4. **Logging**: Enable detailed logging for monitoring
5. **Model Versioning**: Track model versions for reproducibility

## 📝 License

MIT License - See LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

Built with ❤️ using PyTorch, Transformers, and modern web technologies.
