from flask import Flask, request, Response
import os
import openai

# Load OpenAI API Key from environment (Render)
openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)

def doctor_report(age, stress, mood, sleep, study, activity, screen):

    prompt = f"""
You are a professional mental health doctor.

Patient details:
Age: {age}
Stress level: {stress}
Mood: {mood}
Sleep hours per day: {sleep}
Study hours per day: {study}
Physical activity level: {activity}
Screen time hours per day: {screen}

Give a clear clinical mental health assessment.
Write 6 to 7 meaningful lines.
Use professional but simple doctor language.
Give reassurance and advice.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a licensed mental health professional."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )

    return response.choices[0].message.content



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
<title>AI Mental Health Clinical System</title>
<style>
body {{
    font-family: Arial, sans-serif;
    background: radial-gradient(circle at top, #0f2027, #000);
    color: white;
    text-align: center;
    padding: 40px;
}}
.card {{
    width: 440px;
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
<h1>🧠 AI Mental Health Clinical System</h1>
<h3>SRICHARAN NADAKUDURU<br>CSD – College Project 2026</h3>

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

<button type="submit">Generate AI Doctor Report</button>
</form>
</div>

{result_html}

</body>
</html>
"""


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

