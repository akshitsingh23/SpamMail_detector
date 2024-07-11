from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib  # Assuming you are using joblib to load a pre-trained model
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load your pre-trained model (modify the path as needed)
model = pickle.load(open('./spam_mail_detector.pkl', 'rb'))
vectorizer = pickle.load(open('./vectorizer.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # print(data)
    email_text = data['email']
    
    # Transform the input text using the vectorizer
    email_vector = vectorizer.transform([email_text])
    # print(email_vector)
    # Make a prediction
    prediction = model.predict(email_vector)
    # print(prediction)
    
    # Convert the prediction to a human-readable format
    result = 'Spam Mail' if prediction[0] == 0 else 'Valid Mail'
    print(prediction[0])

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
