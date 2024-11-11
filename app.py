from flask import Flask, request, render_template
from flask_cors import CORS
from transformers import ElectraForSequenceClassification, ElectraTokenizer
import torch

app = Flask(__name__)
CORS(app)

# Load the model and tokenizer
model_path = 'saved_model/hybrid'
model = ElectraForSequenceClassification.from_pretrained(model_path)
tokenizer = ElectraTokenizer.from_pretrained(model_path)

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1).item()
    return predictions

@app.route('/', methods=['GET', 'POST'])
def home():
    sentiment = None
    review_text = None
    if request.method == 'POST':
        review_text = request.form.get('review')
        if review_text:
            prediction = predict_sentiment(review_text)
            sentiment_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
            sentiment = sentiment_map.get(prediction, "Unknown")
    return render_template('index.html', sentiment=sentiment, review=review_text)

if __name__ == '__main__':
    app.run(debug=True)
