from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("bmi_model.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    height = data['height']
    weight = data['weight']

    prediction = model.predict([[height, weight]])

    return jsonify({'result': prediction[0]})

if __name__ == '__main__':
    app.run()
