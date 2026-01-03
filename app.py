from flask import Flask, request, Response
import os

app = Flask(__name__)

def doctor_report(age, stress, mood, sleep, study, activity, screen):
    risk = 0
    report = ""

    # Risk scoring
    if stress == "High": risk += 3
    elif stress == "Medium": risk += 2

    if mood == "Hyperactive": risk += 2
    elif mood == "Active": risk += 1

    if sleep < 6: risk += 3
    elif sleep < 7: risk += 2

    if study > 8: risk += 2
    if activity == "Low": risk += 2
    if screen > 7: risk += 2

    # Doctor-style report
    report += "CLINICAL MENTAL HEALTH ASSESSMENT\n\n"
    report += f"Age Group Analysis: At {age} years, mental health is highly influenced by lifestyle patterns.\n\n"

    if risk >= 10:
        report += (
            "Overall Risk Level: HIGH\n\n"
            "Clinical Interpretation:\n"
            "- Indicators suggest mental overload and elevated stress response.\n"
            "- Irregular sleep and prolonged screen exposure are major contributors.\n"
            "- Current routine may lead to burnout if continued.\n\n"
            "Doctor’s Advice:\n"
            "- Ensure 7–8 hours of uninterrupted sleep daily.\n"
            "- Reduce screen usage, especially before bedtime.\n"
            "- Introduce physical activity (30 minutes/day).\n"
            "- Practice relaxation techniques such as breathing or meditation.\n"
            "- Academic workload should be spaced with proper breaks.\n"
            "- If symptoms persist, professional counselling is strongly advised.\n"
        )

    elif risk >= 6:
        report += (
            "Overall Risk Level: MODERATE\n\n"
            "Clinical Interpretation:\n"
            "- Mild to moderate stress patterns detected.\n"
            "- Lifestyle imbalance is present but reversible.\n\n"
            "Doctor’s Advice:\n"
            "- Maintain consistent sleep timings (minimum 7 hours).\n"
            "- Balance study hours with short mental breaks.\n"
            "- Limit continuous screen exposure.\n"
            "- Engage in light physical activities.\n"
            "- Monitor stress levels weekly.\n"
        )

    else:
        report += (
            "Overall Risk Level: STABLE\n\n"
            "Clinical Interpretation:\n"
            "- Mental health indicators are within healthy limits.\n"
            "- Current lifestyle supports emotional stability.\n\n"
            "Doctor’s Advice:\n"
            "- Continue maintaining a balanced routine.\n"
            "- Avoid sudden increases in workload.\n"
            "- Preserve good sleep hygiene.\n"
            "- Stay physically and socially active.\n"
        )

    report += (
        "\nNote:\n"
        "This assessment is preventive in nature and not a medical diagnosis."
    )

    return report


@app.route("/", methods=["GET", "POST", "HEAD"])
def home():
    if request.method == "HEAD":
        return Response(status=200)

    result_html = ""

    if request.method == "POST":
        report = doctor_report(
            int(request.form["age"]),
            request.form["stress"],
            request.form["mood"],
            int(request.form["sleep"]),
            int(request.form["study"]),
            request.form["activity"],
            int(request.form["screen"])
        )
        result_html = f"<pre>{report}</pre>"

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>Mental Health Clinical Assessment</title>
<style>
body {{
    font-family: Arial, sans-serif;
    background: radial-gradient(circle at top, #0f2027, #000);
    color: white;
    text-align: center;
    padding: 40px;
}}
.card {{
    width: 420px;
    margin: auto;
    padding: 25px;
    background: rgba(255,255,255,0.1);
    border-radius: 15px;
}}
input, select {{
    width: 95%;
    padding: 10px;
    margin: 8px 0;
    border-radius: 8px;
    border: none;
}}
button {{
    padding: 12px 30px;
    border-radius: 25px;
    background: cyan;
    border: none;
    cursor: pointer;
}}
pre {{
    text-align: left;
    margin-top: 25px;
    background: rgba(0,0,0,0.6);
    padding: 20px;
    border-left: 4px solid cyan;
}}
</style>
</head>

<body>
<h1>🧠 Mental Health Clinical System</h1>
<h3>Sricharan Nadakuduru | CSD | 2026</h3>

<div class="card">
<form method="post">
<input type="number" name="age" placeholder="Age (1–100)" required>

<select name="stress" required>
<option value="">Stress Level</option>
<option>Low</option>
<option>Medium</option>
<option>High</option>
</select>

<select name="mood" required>
<option value="">Mood Type</option>
<option>Calm</option>
<option>Active</option>
<option>Hyperactive</option>
</select>

<input type="number" name="sleep" placeholder="Sleep Hours" required>
<input type="number" name="study" placeholder="Study Hours" required>

<select name="activity" required>
<option value="">Physical Activity</option>
<option>Low</option>
<option>Moderate</option>
<option>High</option>
</select>

<input type="number" name="screen" placeholder="Screen Time (hrs/day)" required>

<button type="submit">Generate Doctor Report</button>
</form>
</div>

{result_html}

</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

