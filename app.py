from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Premium Mental Wellness Portal</title>

<style>
/* -------- RESET -------- */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* -------- BODY -------- */
body {
    height: 100vh;
    background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #000000);
    background-size: 400% 400%;
    animation: gradientMove 18s ease infinite;
    font-family: 'Segoe UI', sans-serif;
    color: white;
    overflow: hidden;
}

/* -------- BACKGROUND ANIMATION -------- */
@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* -------- FLOATING ORBS -------- */
.orb {
    position: absolute;
    width: 220px;
    height: 220px;
    background: radial-gradient(circle, rgba(0,255,255,0.6), transparent);
    border-radius: 50%;
    filter: blur(40px);
    animation: float 14s infinite alternate ease-in-out;
}

.orb.one { top: 10%; left: 15%; }
.orb.two { bottom: 10%; right: 15%; animation-delay: 4s; }
.orb.three { top: 50%; right: 40%; animation-delay: 8s; }

@keyframes float {
    from { transform: translateY(0px); }
    to { transform: translateY(-120px); }
}

/* -------- MAIN CARD -------- */
.container {
    position: relative;
    z-index: 2;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.card {
    width: 520px;
    padding: 40px;
    background: rgba(255,255,255,0.08);
    border-radius: 25px;
    backdrop-filter: blur(15px);
    box-shadow: 0 0 60px rgba(0,255,255,0.35);
    text-align: center;
    animation: fadeIn 2s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: scale(0.9); }
    to { opacity: 1; transform: scale(1); }
}

/* -------- TEXT -------- */
h1 {
    font-size: 2.6em;
    text-shadow: 0 0 25px cyan;
}

.subtitle {
    margin-top: 10px;
    font-size: 1.1em;
    opacity: 0.9;
}

.identity {
    margin-top: 25px;
    padding: 15px;
    border-radius: 15px;
    background: rgba(0,0,0,0.4);
    box-shadow: inset 0 0 20px rgba(0,255,255,0.2);
}

.identity h3 {
    color: cyan;
}

/* -------- BUTTON -------- */
button {
    margin-top: 30px;
    padding: 14px 40px;
    font-size: 1em;
    border: none;
    border-radius: 30px;
    background: linear-gradient(90deg, cyan, #00ffaa);
    color: black;
    cursor: pointer;
    box-shadow: 0 0 25px cyan;
    transition: transform 0.3s, box-shadow 0.3s;
}

button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 45px cyan;
}

/* -------- FOOTER -------- */
.footer {
    margin-top: 20px;
    font-size: 0.85em;
    opacity: 0.6;
}
</style>
</head>

<body>

<div class="orb one"></div>
<div class="orb two"></div>
<div class="orb three"></div>

<div class="container">
    <div class="card">
        <h1>🌌 Mental Wellness Experience</h1>
        <p class="subtitle">A Premium Cinematic Interface</p>

        <div class="identity">
            <h3>SRICHARAN NADAKUDURU</h3>
            <p>CSD | College Project | 2026</p>
        </div>

        <button>Explore Experience</button>

        <div class="footer">
            Designed with motion, depth & visual intelligence
        </div>
    </div>
</div>

</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
