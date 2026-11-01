from flask import Flask, request, jsonify
import joblib


app = Flask(__name__)

model = joblib.load("student_result_model.pkl")


@app.route("/")
def home():
    return jsonify({
        "message": "Student Result Prediction API"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = [[
        data["attendance"],
        data["internal_marks"],
        data["assignment_marks"],
        data["previous_score"]
    ]]

    prediction = int(model.predict(features)[0])

    if prediction == 1:
        result = "PASS"
    else:
        result = "FAIL"

    return jsonify({
        "prediction": result,
        "prediction_code": prediction
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
