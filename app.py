from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)
CORS(app)

# HuggingFace repo
HF_REPO = "moizsheraz/phishing-detection-model"

# Load model from HuggingFace Hub
try:
    tokenizer = AutoTokenizer.from_pretrained(HF_REPO)
    model = AutoModelForSequenceClassification.from_pretrained(HF_REPO)
    model.eval()
    print("✓ Model loaded from HuggingFace Hub!")
except Exception as e:
    print(f"⚠ Failed to load model: {e}")
    model, tokenizer = None, None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 503
    
    text = request.json.get('text', '').lower()
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    inputs = tokenizer(
        text,
        truncation=True,
        padding=True,
        max_length=512,
        return_tensors="pt"
    )
    
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        pred = torch.argmax(probs, dim=1).item()
        conf = probs[0][pred].item()
    
    return jsonify({
        "prediction": "Phishing" if pred == 1 else "Legitimate",
        "is_phishing": pred == 1,
        "confidence": round(conf * 100, 2),
        "probabilities": {
            "legitimate": round(probs[0][0].item() * 100, 2),
            "phishing": round(probs[0][1].item() * 100, 2)
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
