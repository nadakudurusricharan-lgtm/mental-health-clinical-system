from flask import Flask, render_template, request

app = Flask(__name__)

def doctor_report(age, stress, mood, sleep, study, activity, screen):
    report = ""

    # AGE CONTEXT
    report += f"PATIENT PROFILE:\n"
    report += f"Age Group: {age} years\n\n"

    # INITIAL ASSESSMENT
    report += "CLINICAL ASSESSMENT:\n"

    risk_score = 0

    # Stress
    if stress == "High":
        report += "- High perceived stress detected.\n"
        risk_score += 3
    elif stress == "Medium":
        report += "- Moderate stress levels detected.\n"
        risk_score += 2
    else:
        report += "- Stress levels appear controlled.\n"
        risk_score += 1

    # Mood
    if mood == "Hyperactive":
        report += "- Hyperactive mood indicates possible mental overload.\n"
        risk_score += 2
    elif mood == "Active":
        report += "- Active mood is acceptable but needs balance.\n"
        risk_score += 1
    else:
        report += "- Calm mood indicates emotional stability.\n"

    # Sleep
    if sleep < 6:
        report += "- Inadequate sleep duration (below healthy range).\n"
        risk_score += 3
    elif sleep < 7:
        report += "- Slightly reduced sleep duration.\n"
        risk_score += 2
    else:
        report += "- Sleep duration is within healthy range.\n"

    # Study Load
    if study > 8:
        report += "- Excessive study load detected.\n"
        risk_score += 2
    elif study > 6:
        report += "- Moderate academic load.\n"
        risk_score += 1

    # Physical Activity
    if activity == "Low":
        report += "- Low physical activity contributes to mental fatigue.\n"
        risk_score += 2
    elif activity == "Moderate":
        report += "- Moderate physical activity supports mental health.\n"
    else:
        report += "- Good physical activity level detected.\n"

    # Screen Time
    if screen > 7:
        report += "- Excessive screen exposure observed.\n"
        risk_score += 2
    elif screen > 5:
        report += "- Moderate screen exposure.\n"
        risk_score += 1

    # FINAL RISK
    report += "\nFINAL CLINICAL OPINION:\n"

    if risk_score >= 10:
        report += (
            "Overall mental health risk is HIGH.\n\n"
            "DOCTOR'S ADVICE:\n"
            "- Immediate reduction of mental and screen overload\n"
            "- Minimum 7–8 hours of sleep daily\n"
            "- Daily physical activity (at least 30 minutes)\n"
            "- Stress management techniques recommended\n"
            "- Counselling support strongly advised\n"
        )
    elif risk_score >= 6:
        report += (
            "Overall mental health risk is MODERATE.\n\n"
            "DOCTOR'S ADVICE:\n"
            "- Improve sleep consistency\n"
            "- Balance study and relaxation\n"
            "- Reduce screen exposure before bedtime\n"
            "- Monitor stress weekly\n"
        )
    else:
        report += (
            "Overall mental health status is STABLE.\n\n"
            "DOCTOR'S ADVICE:\n"
            "- Maintain current healthy routine\n"
            "- Continue balanced lifestyle\n"
            "- Avoid sudden increases in workload\n"
        )

    report += (
        "\nDISCLAIMER:\n"
        "This is a preventive clinical assessment system and not a medical diagnosis."
    )

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

        result = doctor_report(age, stress, mood, sleep, study, activity, screen)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)


