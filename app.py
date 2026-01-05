from flask import Flask, request, render_template_string

app = Flask(__name__)

# ------------------ DECISION ENGINE ------------------
def generate_report(data):
    score = 0

    # Age factor
    if data["age"] < 18 or data["age"] > 60:
        score += 1

    # Stress
    if data["stress"] == "High":
        score += 3
    elif data["stress"] == "Medium":
        score += 2

    # Study overload
    if data["study"] > 8:
        score += 2

    # Screen time
    if data["screen"] > 7:
        score += 2

    # Physical activity
    if data["activity"] == "Low":
        score += 2
    elif data["activity"] == "Moderate":
        score += 1

    # Sleep
    if data["sleep"] < 6:
        score += 3
    elif data["sleep"] < 7:
        score += 2

    # Mood (Calm / Active / Hyperactive)
    if data["mood"] == "Hyperactive":
        score += 2
    elif data["mood"] == "Active":
        score += 1
    # Calm adds 0

    # Decision
    if score >= 10:
        level = "HIGH RISK"
        advice = [
            "Clinical indicators suggest significant mental overload.",
            "Sustained stress combined with insufficient sleep is evident.",
            "Cognitive fatigue may impair focus and emotional regulation.",
            "Immediate lifestyle restructuring is strongly recommended.",
            "Reduce screen exposure and normalize sleep routines.",
            "Daily physical activity is essential for recovery.",
            "Professional mental health consultation should be considered."
        ]
    elif score >= 6:
        level = "MODERATE RISK"
        advice = [
            "Early signs of mental strain have been identified.",
            "Irregular routines may be affecting emotional balance.",
            "Stress management techniques should be practiced daily.",
            "Improving sleep consistency can enhance mental clarity.",
            "Balanced study–rest cycles are advised.",
            "Regular physical activity will support recovery."
        ]
    else:
        level = "STABLE"
        advice = [
            "Mental health indicators are currently within healthy limits.",
            "Lifestyle balance appears adequate and sustainable.",
            "Sleep and activity patterns support cognitive performance.",
            "Stress levels are being managed effectively.",
            "Continue maintaining structured daily routines.",
            "Preventive self-care will sustain long-term wellbeing."
        ]

    return level, advice


# ------------------ ROUTE ------------------
@app.route("/", methods=["GET", "POST"])
def home():
    level = ""
    advice = []

    if request.method == "POST":
        data = {
            "age": int(request.form["age"]),
            "stress": request.form["stress"],
            "study": int(request.form["study"]),
            "screen": int(request.form["screen"]),
            "activity": request.form["activity"],
            "sleep": int(request.form["sleep"]),
            "mood": request.form["mood"],
        }
        level, advice = generate_report(data)

    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Premium Mental Wellness System</title>

<style>
/* -------- GLOBAL -------- */
body{
    margin:0;
    font-family:'Segoe UI',sans-serif;
    background:linear-gradient(120deg,#020024,#090979,#000);
    color:white;
    overflow-x:hidden;
}

/* -------- MOVING BACKGROUND -------- */
.bg{
    position:fixed;
    width:220%;
    height:220%;
    background:radial-gradient(circle,rgba(0,255,255,.15),transparent);
    animation:floatBG 20s infinite alternate ease-in-out;
    z-index:0;
}
@keyframes floatBG{
    from{transform:translate(0,0)}
    to{transform:translate(-300px,-300px)}
}

/* -------- SECTIONS -------- */
section{
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    position:relative;
    z-index:2;
}

/* -------- GLASS CARD -------- */
.card{
    width:560px;
    padding:40px;
    background:rgba(255,255,255,.1);
    backdrop-filter:blur(20px);
    border-radius:26px;
    box-shadow:0 0 60px rgba(0,255,255,.45);
    text-align:center;
}

/* -------- INPUTS -------- */
input,select{
    width:95%;
    padding:12px;
    margin:8px;
    border-radius:10px;
    border:none;
}

/* -------- BUTTON -------- */
button{
    margin-top:20px;
    padding:14px 40px;
    border-radius:30px;
    border:none;
    background:linear-gradient(90deg,cyan,#00ffaa);
    box-shadow:0 0 30px cyan;
    cursor:pointer;
    transition:.3s;
}
button:hover{
    transform:scale(1.08);
    box-shadow:0 0 50px cyan;
}

/* -------- OUTPUT -------- */
.output{
    margin-top:25px;
    text-align:left;
    background:rgba(0,0,0,.65);
    padding:20px;
    border-left:4px solid cyan;
    border-radius:8px;
}

/* -------- SCROLL REVEAL -------- */
.reveal{
    opacity:0;
    transform:translateY(60px);
    transition:1s;
}
.reveal.active{
    opacity:1;
    transform:none;
}

/* -------- MOOD COLOR HINT -------- */
.mood-calm{ box-shadow:0 0 40px rgba(0,200,255,.35); }
.mood-active{ box-shadow:0 0 40px rgba(255,215,0,.35); }
.mood-hyper{ box-shadow:0 0 40px rgba(255,80,80,.45); }
</style>
</head>

<body>

<div class="bg"></div>

<section>
<div class="card reveal" id="mainCard">
<h1>🧠 Mental Wellness Analyzer</h1>
<p><b>SRICHARAN NADAKUDURU</b><br>CSD | College Project | 2026</p>

<form method="post" onsubmit="clickSound()">
<input name="age" placeholder="Age" required>

<select name="stress">
  <option>Low</option>
  <option>Medium</option>
  <option>High</option>
</select>

<input name="study" placeholder="Study Hours" required>
<input name="screen" placeholder="Screen Time (hrs/day)" required>

<select name="activity">
  <option>Low</option>
  <option>Moderate</option>
  <option>High</option>
</select>

<input name="sleep" placeholder="Sleep Hours" required>

<select name="mood" id="moodSelect">
  <option>Calm</option>
  <option>Active</option>
  <option>Hyperactive</option>
</select>

<button>Generate Clinical Report</button>
</form>

{% if level %}
<div class="output">
<h3>Assessed Risk Level: {{ level }}</h3>
<ul>
{% for a in advice %}
<li>{{ a }}</li>
{% endfor %}
</ul>
</div>
{% endif %}
</div>
</section>

<audio id="click">
  <source src="https://www.soundjay.com/buttons/sounds/button-16.mp3">
</audio>

<script>
// Scroll reveal
window.addEventListener("scroll",()=>{
  document.querySelectorAll(".reveal").forEach(el=>{
    if(el.getBoundingClientRect().top < window.innerHeight-120){
      el.classList.add("active");
    }
  });
});

// Mouse parallax
document.addEventListener("mousemove",e=>{
  document.querySelector(".bg").style.transform =
    "translate("+(e.clientX*0.03)+"px,"+(e.clientY*0.03)+"px)";
});

// Click sound
function clickSound(){
  document.getElementById("click").play();
}

// Mood-based glow
const moodSelect = document.getElementById("moodSelect");
const card = document.getElementById("mainCard");
moodSelect.addEventListener("change", ()=>{
  card.classList.remove("mood-calm","mood-active","mood-hyper");
  if(moodSelect.value==="Calm") card.classList.add("mood-calm");
  if(moodSelect.value==="Active") card.classList.add("mood-active");
  if(moodSelect.value==="Hyperactive") card.classList.add("mood-hyper");
});
</script>

</body>
</html>
""", level=level, advice=advice)

if __name__ == "__main__":
    app.run()
