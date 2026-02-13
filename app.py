import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Arshu ❤️", layout="centered")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Confetti -->
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

<style>

body {
    margin:0;
    height:100vh;
    overflow:hidden;
    font-family: 'Segoe UI', sans-serif;
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
    transition: background 1.5s ease;
}

/* Cinematic Fade */
.fade-screen {
    position:fixed;
    width:100%;
    height:100%;
    background:black;
    top:0;
    left:0;
    opacity:0;
    pointer-events:none;
    transition: opacity 1s ease;
    z-index:999;
}

h1, h2 {
    color:white;
    text-align:center;
}

button {
    padding:15px 35px;
    font-size:18px;
    border:none;
    border-radius:40px;
    cursor:pointer;
    margin:10px;
}

#yesBtn {
    background:#ff1744;
    color:white;
}

#noBtn {
    background:white;
    color:#ff1744;
    position:absolute;
}

#page2, #page3, #page4 {
    display:none;
    text-align:center;
}

.teddy {
    width:300px;
}

.beagle {
    width:200px;
    position:absolute;
    left:-250px;
    bottom:50px;
    animation: runDog 5s linear forwards;
}

@keyframes runDog {
    from { left:-250px; }
    to { left:110%; }
}

.envelope {
    width:150px;
    cursor:pointer;
    transition: transform 0.5s;
}

.envelope:hover {
    transform: scale(1.1);
}

.open-letter {
    animation: openLetter 1s forwards;
}

@keyframes openLetter {
    from { transform: scaleY(0); }
    to { transform: scaleY(1); }
}

</style>
</head>

<body>

<div class="fade-screen" id="fade"></div>

<!-- PAGE 1 -->
<div id="page1">
    <!-- Beautiful Real Teddy Image -->
    <img 
    src="https://images.unsplash.com/photo-1601758123927-1962f0d6a3c6?auto=format&fit=crop&w=500&q=80" 
    style="width:250px; border-radius:20px; box-shadow:0 10px 30px rgba(0,0,0,0.4); margin-bottom:20px;">

    <h1>Hey my dear Arshu 💖<br>Will you be my Valentine baby?</h1>
    <div style="margin-top:40px; position:relative;">
        <button id="yesBtn" onclick="goToPage2()">Yes 💕</button>
        <button id="noBtn">No 😢</button>
    </div>
</div>

<!-- PAGE 2 -->
<div id="page2">
    <img class="teddy" src="https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif">
    <h2>Thanks for accepting my Love baby ❤️</h2>
</div>

<!-- PAGE 3 -->
<div id="page3">
    <h2>Hey Arshu 🐶 You have a message from Mano 💌</h2>
    <img class="beagle" src="https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif">
    <br><br>
    <img class="envelope" onclick="openLetter()"
    src="https://cdn-icons-png.flaticon.com/512/561/561127.png">
</div>

<!-- PAGE 4 -->
<div id="page4">
    <div id="letterContent" style="display:none; color:white; max-width:700px; font-size:18px;">
        <h2>My Letter To You 💌</h2>
        Hey my Paanda 🐼 <br><br>
        Ennaku namma Angappa School kudutha biggest gift na… adhu nee tha ma. School mudinja apram neraiya memories marandhuduchu, aana nee mattum en life la irundhu marave illa.

        Naan eppovum nenachu kooda paakala, naan unna ivalo love pannuven nu. Andha oru varusham nee en kooda irundha appo, naan feel panradhu love nu enakku puriyala maa. Adhu oru comfort nu dhaan nenachen… oru close bond nu nenachen. Aana nee en life la irundhu thooram pona apram dhaan purinjadhu — adhu ellam love dhaan nu.

        Unna theda aarambichiten. Unna romba miss pannen di maa. Unna tholachuten nu nenacha neraya naal azhudhuruke… silenta sogama irundhuruke… zone out aayuruke. Un absence enakku evlo impact pannudhu nu appo dhaan purinjadhu.

        Aana kanavula kooda nenachu paakala… 13 varusham apram namma thirumba pesuvom nu. Ippo namma irukkara bond… adhu enakku romba precious maa. Idhu destiny illati enna nu theriyala.

        Eppovadhu nee yosichu paathurukiya… “Naanum Mano-um oru life start pannina eppudi irukkum nu?"
        Naan daily yosippen. Un kooda oru simple life… morning coffee share panradhu, chinna chinna sandai, adhukku apram patch up, un kitta safe-aa thookam varradhu… idhu ellam naan neraya thadava imagine panniruken.

        Unkitta irundhu enakku real life la kedaikaadha paasamum love-um… en kanavula kedaichirukku. Naan romba safe-aa feel pannuve un kitta. Nee enkitta konjam ownership edukkara maari pesumbodhu… adhu enakku romba pidikkum. Naan ennoda paadhi life-ah un kooda kanavula dhaan vaazhndhuruke ma.

        Unnaku enna bayam, enna problem nu enakku puriyudhu. Naan rush panna maaten. Nee un time eduthuko. Oru naal un manasukulla strong-aa “Mano dhaan en life partner” nu feel vandha… unakku en mela complete trust vandha… appo nee enkitta vaa.

        Naan unna Raani maari vechu paathupen. Un Amma-um, en Amma-um “Chaa ippadi oru husband namakku kedaikalaye” nu rombo porama padra maari unna sandhoshama vechupen.

        Aana idhu ellathukum munnaadi…
        Nee en mela love-um trust-um vechuttu, en kooda vaazha dhairiyama irukanum. Adhu dhaan en aasai.Apdi oru time varumbodhu....
        <br><br>
        <b>Seekaram enna marriage panniko di thangame ❤️</b>
    </div>
</div>

<!-- Romantic Background Music -->
<audio id="bgMusic" autoplay loop>
  <source src="https://www.bensound.com/bensound-music/bensound-romantic.mp3" type="audio/mp3">
</audio>

<script>

// Move NO button
const noBtn = document.getElementById("noBtn");
noBtn.addEventListener("mouseover", function() {
    const x = Math.random() * (window.innerWidth - 100);
    const y = Math.random() * (window.innerHeight - 100);
    noBtn.style.left = x + "px";
    noBtn.style.top = y + "px";
});

function fadeTransition(callback){
    const fade = document.getElementById("fade");
    fade.style.opacity = 1;
    setTimeout(()=>{
        callback();
        fade.style.opacity = 0;
    },1000);
}

function goToPage2(){
    fadeTransition(()=>{
        document.getElementById("page1").style.display="none";
        document.getElementById("page2").style.display="block";
        document.body.style.background="linear-gradient(135deg,#ff512f,#dd2476)";
    });

    setTimeout(()=>{ goToPage3(); },4000);
}

function goToPage3(){
    fadeTransition(()=>{
        document.getElementById("page2").style.display="none";
        document.getElementById("page3").style.display="block";
        document.body.style.background="linear-gradient(135deg,#00c6ff,#0072ff)";
    });
}

function openLetter(){
    fadeTransition(()=>{
        document.getElementById("page3").style.display="none";
        document.getElementById("page4").style.display="block";
        document.body.style.background="linear-gradient(135deg,#ff758c,#ff7eb3)";
        document.getElementById("letterContent").style.display="block";

        // Confetti explosion
        confetti({
            particleCount:200,
            spread:120,
            origin:{y:0.6}
        });
    });
}

</script>

</body>
</html>
"""

components.html(html_code, height=950)
