import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# HuggingFace model repository
HF_REPO = "moizsheraz/phishing-detection-model"

# Load model and tokenizer
try:
    tokenizer = AutoTokenizer.from_pretrained(HF_REPO)
    model = AutoModelForSequenceClassification.from_pretrained(HF_REPO)
    model.eval()
    print("✓ Model loaded successfully from HuggingFace Hub!")
except Exception as e:
    print(f"⚠ Failed to load model: {e}")
    model, tokenizer = None, None

def predict_phishing(email_text):
    """
    Predict if an email is phishing or legitimate
    
    Args:
        email_text: The email content to analyze
    
    Returns:
        Prediction result with confidence scores
    """
    if model is None or tokenizer is None:
        return "❌ Model not loaded. Please check the configuration."
    
    if not email_text or not email_text.strip():
        return "⚠️ Please enter email content to analyze."
    
    # Preprocess and tokenize
    text = email_text.lower()
    inputs = tokenizer(
        text,
        truncation=True,
        padding=True,
        max_length=512,
        return_tensors="pt"
    )
    
    # Make prediction
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        pred = torch.argmax(probs, dim=1).item()
        conf = probs[0][pred].item()
        
        legitimate_prob = probs[0][0].item()
        phishing_prob = probs[0][1].item()
    
    # Format result
    if pred == 1:  # Phishing
        result = f"""
## ⚠️ PHISHING DETECTED

**Confidence:** {conf * 100:.2f}%

### Probability Breakdown:
- 🔴 **Phishing:** {phishing_prob * 100:.2f}%
- 🟢 **Legitimate:** {legitimate_prob * 100:.2f}%

### ⚠️ Warning
This email appears to be a phishing attempt. Be cautious and:
- Do not click any links
- Do not download attachments
- Do not provide personal information
- Report this email to your IT department
"""
    else:  # Legitimate
        result = f"""
## ✅ LEGITIMATE EMAIL

**Confidence:** {conf * 100:.2f}%

### Probability Breakdown:
- 🟢 **Legitimate:** {legitimate_prob * 100:.2f}%
- 🔴 **Phishing:** {phishing_prob * 100:.2f}%

### ℹ️ Note
This email appears to be legitimate, but always remain vigilant:
- Verify sender identity
- Check for suspicious links
- Be cautious with sensitive information
"""
    
    return result

# Example emails for demonstration
examples = [
    ["""Dear Customer,

Your account has been compromised! Click here immediately to verify your identity:
http://secure-bank-verify.com/update

Failure to verify within 24 hours will result in account suspension.

Best regards,
Security Team"""],
    ["""Hi Team,

The quarterly meeting is scheduled for next Tuesday at 2 PM in Conference Room B.
Please review the attached agenda and come prepared with your updates.

Looking forward to seeing everyone there.

Best,
Sarah"""],
    ["""URGENT: You've won $1,000,000!

Congratulations! You have been selected as the winner of our international lottery.
To claim your prize, please send us your bank details and pay a processing fee of $500.

Click here to claim: http://lottery-winner-claim.com

Act fast, this offer expires in 48 hours!"""]
]

# Create Gradio interface
with gr.Blocks(theme=gr.themes.Soft(), title="🛡️ PhishGuard AI") as demo:
    gr.Markdown("""
    # 🛡️ PhishGuard AI - Phishing Email Detection
    
    Detect phishing emails using advanced BERT-based AI model. Simply paste an email and click analyze!
    
    **Powered by:** BERT (Bidirectional Encoder Representations from Transformers)
    """)
    
    with gr.Row():
        with gr.Column():
            email_input = gr.Textbox(
                label="📧 Email Content",
                placeholder="Paste the email content here...",
                lines=10,
                max_lines=20
            )
            
            with gr.Row():
                analyze_btn = gr.Button("🔍 Analyze Email", variant="primary", size="lg")
                clear_btn = gr.ClearButton([email_input], value="🗑️ Clear", size="lg")
    
    with gr.Row():
        output = gr.Markdown(label="Analysis Result")
    
    # Connect the button to the prediction function
    analyze_btn.click(
        fn=predict_phishing,
        inputs=email_input,
        outputs=output
    )
    
    # Add examples section
    gr.Markdown("### 📝 Try These Examples:")
    gr.Examples(
        examples=examples,
        inputs=email_input,
        label="Example Emails"
    )
    
    gr.Markdown("""
    ---
    ### ℹ️ About This Tool
    
    This AI-powered tool uses a fine-tuned BERT model to detect phishing emails. It analyzes the email content 
    and provides a confidence score indicating whether the email is legitimate or a phishing attempt.
    
    **Note:** This is a demo tool. Always use your judgment and follow your organization's security policies.
    
    **Model:** [moizsheraz/phishing-detection-model](https://huggingface.co/moizsheraz/phishing-detection-model)
    """)

# Launch the app
if __name__ == "__main__":
    demo.launch()
