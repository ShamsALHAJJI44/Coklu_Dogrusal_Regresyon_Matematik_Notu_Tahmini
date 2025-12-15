from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    # Numerical inputs
    reading = float(request.form["reading"])
    writing = float(request.form["writing"])
    gender_male = float(request.form["gender_male"])

    # ----- RACE / ETHNICITY -----
    race = request.form["race"]  # A/B/C/D/E but A is baseline (dropped dummy)
    groupB = 1 if race == "B" else 0
    groupC = 1 if race == "C" else 0
    groupD = 1 if race == "D" else 0
    groupE = 1 if race == "E" else 0

    # ----- PARENT EDUCATION -----
    parent = request.form["parent_edu"]
    parent_bachelor = 1 if parent == "bachelor" else 0
    parent_highschool = 1 if parent == "highschool" else 0
    parent_master = 1 if parent == "master" else 0
    parent_college = 1 if parent == "somecollege" else 0
    parent_someHS = 1 if parent == "somehs" else 0
    # baseline = associate's degree (dropped dummy)

    # ----- LUNCH -----
    lunch_standard = float(request.form["lunch"])

    # ----- TEST PREPARATION -----
    test_none = float(request.form["testprep"])

    # Create final numpy array with correct order
    input_data = np.array([[reading, writing, gender_male,
                            groupB, groupC, groupD, groupE,
                            parent_bachelor, parent_highschool, parent_master,
                            parent_college, parent_someHS,
                            lunch_standard, test_none]])

    prediction = model.predict(input_data)[0]

    return render_template("index.html",
                           prediction_text=f"Predicted Math Score = {prediction:.2f}")

if __name__ == "__main__":
    app.run(debug=True)
