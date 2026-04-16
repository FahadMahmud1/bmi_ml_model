from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the ML model
with open('bmi_model.pkl', 'rb') as f:
    model = pickle.load(f)

print(" Model loaded successfully!")

@app.route('/')
def home():
    return "BMI Prediction API is running! "

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data sent from Flutter
        data = request.json
        height = float(data['height'])
        weight = float(data['weight'])

        print(f"Received → Height: {height}, Weight: {weight}")

        # Run the ML model
        features = [[height, weight]]
        prediction = model.predict(features)

        # Convert result to label
        if prediction[0] == 1:
            result = "Overweight"
            message = "You should consider a healthier diet and exercise."
        else:
            result = "Normal Weight"
            message = "Great! Keep maintaining your healthy lifestyle."

        print(f"Prediction → {result}")

        # Send result back to Flutter
        return jsonify({
            'status': 'success',
            'result': result,
            'message': message,
            'height': height,
            'weight': weight
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)