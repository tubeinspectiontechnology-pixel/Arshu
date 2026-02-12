import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Arshu ❤️", layout="centered")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Confetti Library -->
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

<style>

body {
    margin: 0;
    height: 100vh;
    overflow: hidden;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    transition: background 2s ease-in-out;
}

h1 {
    color: white;
    font-size: 45px;
    text-align: center;
    animation: fadeIn 2s ease-in-out;
}

.buttons {
    margin-top: 40px;
    position: relative;
}

button {
    padding: 15px 35px;
    font-size: 20px;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: 0.3s;
    margin: 10px;
}

#yesBtn {
    background-color: #ff1744;
    color: white;
}

#noBtn {
    background-color: white;
    color: #ff1744;
    position: absolute;
}

button:hover {
    transform: scale(1.1);
}

#finalMessage {
    display: none;
    text-align: center;
    color: white;
    padding: 30px;
    animation: zoomIn 2s ease-in-out forwards;
}

@keyframes zoomIn {
    from { transform: scale(0); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}

.teddy-img {
    width: 250px;
    margin-bottom: 20px;
}

.firework {
    position: fixed;
    width: 5px;
    height: 5px;
    background: transparent;
}

canvas {
    position: fixed;
    top: 0;
    left: 0;
    pointer-events: none;
}

</style>
</head>

<body>

<h1 id="question">Hey Arshu, wanna be my Valentine? ❤️</h1>

<div class="buttons">
    <button id="yesBtn" onclick="celebrate()">Yes 💖</button>
    <button id="noBtn">No 😢</button>
</div>

<div id="finalMessage">
    <!-- Teddy Hug GIF -->
    <img class="teddy-img" src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif">
    <h2>Hey my Paanda 🐼</h2>
    <p style="font-size:20px; max-width:700px; margin:auto;">
    You are my only way of happiness.  
    Day by day my love towards you is going beyond the limit.  
    You are the only girl who can make me feel as a complete Man.  
    I just want to spend my rest life with you as your lovable Man.
    Eppovadhu nee think pannirukiya? neeyum naanum serndhu vaazhndha antha life eppudi irrukum nu?
    Naa daily um think pannuve...adhu avalo beautiful ah irrukum.
    Nee eppo bold ah enkitta varuva nu naa wait pannitu irruken.
    Incase unnake en mela love vanthurucha na thn....  
    <br><br>
    <b>Seekaram enna marriage panniko di thangame ❤️</b>
    </p>
</div>

<script>

// Move NO button randomly
const noBtn = document.getElementById("noBtn");

noBtn.addEventListener("mouseover", function() {
    const x = Math.random() * (window.innerWidth - 100);
    const y = Math.random() * (window.innerHeight - 100);
    noBtn.style.left = x + "px";
    noBtn.style.top = y + "px";
});

// Fireworks + Confetti
function celebrate() {

    document.getElementById("question").style.display = "none";
    document.querySelector(".buttons").style.display = "none";
    document.body.style.background = "linear-gradient(135deg, #ff0844, #ffb199)";
    document.getElementById("finalMessage").style.display = "block";

    // Confetti burst
    confetti({
        particleCount: 200,
        spread: 120,
        origin: { y: 0.6 }
    });

    // Continuous fireworks
    var duration = 5 * 1000;
    var animationEnd = Date.now() + duration;

    var interval = setInterval(function() {
        if (Date.now() > animationEnd) {
            return clearInterval(interval);
        }

        confetti({
            particleCount: 50,
            spread: 100,
            origin: {
                x: Math.random(),
                y: Math.random() - 0.2
            }
        });
    }, 300);
}

</script>

</body>
</html>
"""

components.html(html_code, height=900)
