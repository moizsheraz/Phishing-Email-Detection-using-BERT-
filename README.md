# 🛡️ PhishGuard AI - Phishing Email Detection

A modern web application for detecting phishing emails using BERT (Bidirectional Encoder Representations from Transformers). Features both Flask and FastAPI implementations with a sleek cybersecurity-themed UI.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c.svg)
![BERT](https://img.shields.io/badge/BERT-Transformers-yellow.svg)

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

### Option 1: Flask (Recommended for simplicity)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit: `http://localhost:5000`

### Option 2: FastAPI (Recommended for production)

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

- **Real-time Analysis**: Instant phishing detection with confidence scores
- **Batch Processing**: Analyze multiple emails at once
- **Modern UI**: Dark cybersecurity theme with glassmorphism effects
- **Responsive Design**: Works on desktop and mobile
- **Visual Feedback**: Animated confidence meters and status indicators
- **Security Tips**: Context-aware advice based on results

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
