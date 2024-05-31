from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
from scipy.sparse import hstack
import re
import os

app = Flask(__name__)

CORS(app)
# Load the model and vectorizers
vectors = 'vectors'
with open(os.path.join(vectors, 'email_classifier_model.pkl'), 'rb') as file:
    model = pickle.load(file)

with open(os.path.join(vectors, 'subject_vectorizer.pkl'), 'rb') as file:
    subject_vectorizer = pickle.load(file)

with open(os.path.join(vectors, 'body_vectorizer.pkl'), 'rb') as file:
    body_vectorizer = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    json_data = request.json
    subject = json_data['subject'].lower()
    body = json_data['body'].lower()

    subject = re.sub(r'[^a-zA-Z\s]', '', subject)
    body = re.sub(r'[^a-zA-Z\s]', '', body)

    # Transform the subject and body
    subject_vec = subject_vectorizer.transform([subject])
    body_vec = body_vectorizer.transform([body])
    combined_vec = hstack([subject_vec, body_vec])

    
    prediction = model.predict(combined_vec)
    return jsonify({'prediction': 'ham' if prediction[0] == 0 else 'spam'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)