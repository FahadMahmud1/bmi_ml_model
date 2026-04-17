from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("bmi_model.pkl", "rb"))

@app.route('/')
def home():
    return "BMI API is running 🚀"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        height = float(data['height'])
        weight = float(data['weight'])

        prediction = model.predict([[height, weight]])

        if prediction[0] == 1:
            result = "Overweight"
            message = "You should consider diet & exercise."
        else:
            result = "Normal Weight"
            message = "Keep maintaining your healthy lifestyle."

        return jsonify({
            'status': 'success',
            'result': result,
            'message': message
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400
