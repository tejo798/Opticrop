from flask import Flask, render_template, request
import joblib
import webbrowser
from threading import Timer
from crop_data import crop_info   # Import crop information

app = Flask(__name__)

# ---------------- Load Model ----------------
model = joblib.load("model.pkl")


# ---------------- Browser ----------------
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")


# ---------------- Home ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- About ----------------
@app.route("/about")
def about():
    return render_template("about.html")


# ---------------- Dashboard ----------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- Predict Page ----------------
@app.route("/predict")
def predict_page():
    return render_template("predict.html")


# ---------------- Prediction ----------------
@app.route("/predict", methods=["POST"])
def predict():

    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    prediction = model.predict([[N, P, K, temperature, humidity, ph, rainfall]])

    crop = prediction[0].lower()

    info = crop_info.get(
        crop,
        {
            "image": "hero.jpg",
            "description": "Crop information is currently unavailable.",
            "temperature": "-",
            "rainfall": "-",
            "ph": "-",
            "season": "-",
            "fertilizer": "-",
            "tip": "-"
        }
    )

    return render_template(
        "result.html",
        prediction=crop.title(),
        info=info
    )


# ---------------- Run ----------------
if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)