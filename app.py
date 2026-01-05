from flask import Flask, request, Response
import os
from openai import OpenAI

# Create OpenAI client using environment variable
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

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

    html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>AI Mental Health Clinical System</title>

<style>
body {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(120deg, #020024, #090979, #00d4ff);
    background-size: 400% 400%;
    animation: bgMove 15s ease infinite;
    color: white;
}

@keyframes bgMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.container {
    text-align: center;
    padding: 40px 20px;
    animation: fadeIn 2s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.glass {
    width: 450px;
    margin: auto;
    padding: 30px;
    border-radius: 20px;
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(15px);
    box-shadow: 0 0 40px rgba(0,255,255,0.5);
    transition: transform 0.4s;
}

.glass:hover {
    transform: scale(1.03);
}

input, select {
    width: 95%;
    padding: 12px;
    margin: 10px 0;
    border-radius: 10px;
    border: none;
}

button {
    margin-top: 15px;
    padding: 14px 35px;
    border-radius: 30px;
    background: cyan;
    border: none;
    font-size: 1em;
    cursor: pointer;
    box-shadow: 0 0 25px cyan;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { box-shadow: 0 0 10px cyan; }
    50% { box-shadow: 0 0 35px cyan; }
    100% { box-shadow: 0 0 10px cyan; }
}

pre {
    max-width: 800px;
    margin: 40px auto;
    padding: 25px;
    background: rgba(0,0,0,0.6);
    border-left: 5px solid cyan;
    border-radius: 12px;
    white-space: pre-wrap;
    text-align: left;
}

footer {
    margin-top: 40px;
    opacity: 0.7;
    font-size: 0.9em;
}
</style>
</head>

<body>
<div class="container">
    <h1>🧠 AI Mental Health Clinical System</h1>
    <h3>SRICHARAN NADAKUDURU<br>CSD | College Project 2026</h3>

    <div class="glass">
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

    <!-- AI OUTPUT -->
    {{RESULT}}

    <footer>
        ⚠️ AI-based early assessment. Not a medical diagnosis.
    </footer>
</div>
</body>
</html>
"""

    return html.replace("{{RESULT}}", result_html)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
