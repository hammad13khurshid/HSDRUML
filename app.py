import os
from flask import Flask, request, jsonify, render_template
from transformers import RobertaTokenizerFast, RobertaForSequenceClassification
import torch

# Set environment variable to prevent MPS usage
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable CUDA (for GPU) just in case

# Set device to CPU explicitly
device = torch.device('cpu')

# Initialize your Flask app
app = Flask(__name__)

# Load your tokenizer and model
print("Loading tokenizer...")
tokenizer = RobertaTokenizerFast.from_pretrained('/Users/hammadkhurshidchughtaii/Desktop/HSDRUML/model/trained_model')
print("Tokenizer loaded successfully.")

print("Loading model...")
model = RobertaForSequenceClassification.from_pretrained('/Users/hammadkhurshidchughtaii/Desktop/HSDRUML/model/trained_model')
print("Model loaded successfully.")

@app.route('/')
def index():
    print("Rendering index page...")
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    debug_info = []
    
    data = request.json
    text = data.get('text')
    
    debug_info.append("Received text for analysis.")

    if not text:
        return jsonify({'error': 'No text provided', 'debug': debug_info}), 400
    
    # Tokenize and move inputs to CPU
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    debug_info.append("Text tokenized.")

    try:
        # Model inference
        with torch.no_grad():  # Ensure no gradients are calculated
            outputs = model(**inputs)
        debug_info.append("Model inference completed.")
        
        # Get predictions
        predictions = torch.softmax(outputs.logits, dim=1)
        pred_label = torch.argmax(predictions, dim=1).item()
        debug_info.append(f"Prediction: {pred_label}")

        # Directly classify based on the prediction label
        if pred_label == 0:
            hate_speech_type = 'Hate Speech Detected'
        else:
            hate_speech_type = 'No Hate Speech Found'
        debug_info.append(f"Classified as: {hate_speech_type}")

        response = {
            'label': pred_label,
            'type': hate_speech_type,
            'debug': debug_info
        }
        return jsonify(response)
    
    except Exception as e:
        debug_info.append(f"Error during inference: {str(e)}")
        return jsonify({'error': str(e), 'debug': debug_info}), 500

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
