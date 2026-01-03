from flask import Flask, render_template, request
import os

app = Flask(__name__)

def doctor_report(age, stress, mood, sleep, study, activity, screen):
    report = ""

    report += "PATIENT PROFILE:\n"
    report += f"Age: {age} years\n\n"

    report += "CLINICAL ASSESSMENT:\n"
    risk_score = 0

    if stress == "High":
        report += "- High stress levels detected.\n"
        risk_score += 3
    elif stress == "Medium":
        report += "- Moderate stress levels detected.\n"
        risk_score += 2
    else:
        report += "- Stress levels appear controlled.\n"
        risk_score += 1

    if mood == "Hyperactive":
        report += "- Hyperactive mood suggests mental overload.\n"
        risk_score += 2
    elif mood == "Active":
        report += "- Active mood requires balance.\n"
        risk_score += 1
    else:
        report += "- Calm mood indicates emotional stability.\n"

    if sleep < 6:
        report += "- Inadequate sleep duration.\n"
        risk_score += 3
    elif sleep < 7:
        report += "- Slightly reduced sleep duration.\n"
        risk_score += 2
    else:
        report += "- Healthy sleep duration.\n"

    if study > 8:
        report += "- Excessive study load detected.\n"
        risk_score += 2
    elif study > 6:
        report += "- Moderate study load.\n"
        risk_score += 1

    if activity == "Low":
        report += "- Low physical activity.\n"
        risk_score += 2
    elif activity == "Moderate":
        report += "- Moderate physical activity.\n"
    else:
        report += "- Good physical activity level.\n"

    if screen > 7:
        report += "- Excessive screen time.\n"
        risk_score += 2
    elif screen > 5:
        report += "- Moderate screen exposure.\n"
        risk_score += 1

    report += "\nFINAL CLINICAL OPINION:\n"

    if risk_score >= 10:
        report += (
            "Overall mental health risk is HIGH.\n\n"
            "DOCTOR'S ADVICE:\n"
            "- Immediate stress reduction required\n"
            "- Minimum 7–8 hours sleep daily\n"
            "- Reduce screen time\n"
            "- Increase physical activity\n"
            "- Counselling strongly recommended\n"
        )
    elif risk_score >= 6:
        report += (
            "Overall mental health risk is MODERATE.\n\n"
            "DOCTOR'S ADVICE:\n"
            "- Improve sleep consistency\n"
            "- Balance study and relaxation\n"
            "- Monitor stress levels weekly\n"
        )
    else:
        report += (
            "Overall mental health status is STABLE.\n\n"
            "DOCTOR'S ADVICE:\n"
            "- Maintain current healthy routine\n"
            "- Avoid sudden workload increases\n"
        )

    report += "\nDISCLAIMER:\nThis is a preventive assessment, not a medical diagnosis."

    return report


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        age = int(request.form["age"])
        stress = request.form["stress"]
        mood = request.form["mood"]
        sleep = int(request.form["sleep"])
        study = int(request.form["study"])
        activity = request.form["activity"]
        screen = int(request.form["screen"])

        result = doctor_report(
            age, stress, mood, sleep, study, activity, screen
        )

    return render_template("index.html", result=result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

