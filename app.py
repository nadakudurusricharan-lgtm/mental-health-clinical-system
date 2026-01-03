from flask import Flask, request
import os

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Mental Health Clinical Assessment</title>
<style>
body {
    font-family: Arial, sans-serif;
    background: radial-gradient(circle at top, #0f2027, #000);
    color: white;
    text-align: center;
    padding: 40px;
}
.card {
    width: 420px;
    margin: auto;
    padding: 25px;
    background: rgba(255,255,255,0.1);
    border-radius: 15px;
}
input, select {
    width: 95%;
    padding: 10px;
    margin: 8px 0;
    border-radius: 8px;
    border: none;
}
button {
    padding: 12px 30px;
    border-radius: 25px;
    background: cyan;
    border: none;
    cursor: pointer;
}
pre {
    text-align: left;
    margin-top: 25px;
    background: rgba(0,0,0,0.6);
    padding: 20px;
    border-left: 4px solid cyan;
}
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

{result}

</body>
</html>
"""

def doctor_report(age, stress, mood, sleep, study, activity, screen):
    risk = 0
    report = "DOCTOR CLINICAL REPORT\\n\\n"

    if stress == "High": risk += 3
    elif stress == "Medium": risk += 2

    if mood == "Hyperactive": risk += 2
    elif mood == "Active": risk += 1

    if sleep < 6: risk += 3
    elif sleep < 7: risk += 2

    if study > 8: risk += 2
    if activity == "Low": risk += 2
    if screen > 7: risk += 2

    if risk >= 10:
        status = "HIGH RISK"
        advice = "Immediate stress reduction, proper sleep, counselling advised."
    elif risk >= 6:
        status = "MODERATE RISK"
        advice = "Improve lifestyle balance and reduce overload."
    else:
        status = "STABLE"
        advice = "Maintain current healthy routine."

    report += f"Risk Level: {status}\\n\\nDoctor Advice:\\n{advice}"
    return f"<pre>{report}</pre>"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        result = doctor_report(
            int(request.form["age"]),
            request.form["stress"],
            request.form["mood"],
            int(request.form["sleep"]),
            int(request.form["study"]),
            request.form["activity"],
            int(request.form["screen"])
        )
    return HTML_PAGE.format(result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
