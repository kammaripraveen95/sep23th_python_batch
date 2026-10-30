
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NEON RUNNER | Dino Survival</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    background: #050712;
    color: white;
    font-family: Arial, Helvetica, sans-serif;
}

.game-shell {
    width: min(1100px, 95vw);
    position: relative;
    padding: 20px;
    border: 1px solid #273653;
    border-radius: 18px;
    background: linear-gradient(145deg, #10172a, #060914);
    box-shadow: 0 0 60px #00cfff16, 0 0 120px #000;
}

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
    margin-bottom: 18px;
}

.brand {
    font-size: 12px;
    letter-spacing: 5px;
    color: #66eaff;
    font-weight: bold;
}

h1 {
    font-size: clamp(22px, 4vw, 38px);
    letter-spacing: 3px;
    margin-top: 6px;
}

.subtitle {
    font-size: 11px;
    letter-spacing: 3px;
    color: #8795b4;
    margin-top: 7px;
}

.status {
    text-align: right;
    color: #8ca2c7;
    font-size: 11px;
    letter-spacing: 2px;
}

.status span {
    color: #67ffca;
}

.stats {
    display: flex;
    gap: 25px;
    margin: 18px 0;
}

.stat-label {
    font-size: 10px;
    letter-spacing: 2px;
    color: #7e91b5;
}

.stat-value {
    font-size: 24px;
    margin-top: 5px;
    font-weight: bold;
    color: #eafaff;
    font-variant-numeric: tabular-nums;
}

.game {
    position: relative;
    width: 100%;
    height: clamp(260px, 43vw, 390px);
    max-height: 390px;
    overflow: hidden;
    border: 1px solid #284a6b;
    border-radius: 10px;
    background:
        radial-gradient(ellipse at 70% 75%, #17486c 0%, transparent 40%),
        linear-gradient(#080d24 0%, #142d4b 60%, #101b32 100%);
    isolation: isolate;
    cursor: pointer;
    touch-action: manipulation;
}

.game::after {
    content: "";
    position: absolute;
    inset: 0;
    pointer-events: none;
    background: linear-gradient(
        90deg, #02051055, transparent 30%,
        transparent 75%, #02051055
    );
    z-index: 4;
}

.stars {
    position: absolute;
    inset: 0;
    background-image:
        radial-gradient(2px 2px at 10% 15%, white 50%, transparent 60%),
        radial-gradient(1px 1px at 25% 32%, white 50%, transparent 60%),
        radial-gradient(2px 2px at 45% 12%, #a8eaff 50%, transparent 60%),
        radial-gradient(1px 1px at 61% 25%, white 50%, transparent 60%),
        radial-gradient(2px 2px at 83% 13%, white 50%, transparent 60%),
        radial-gradient(1px 1px at 93% 36%, white 50%, transparent 60%),
        radial-gradient(1px 1px at 72% 43%, white 50%, transparent 60%);
    animation: twinkle 3s infinite alternate;
}

@keyframes twinkle {
    from { opacity: .4; }
    to { opacity: 1; }
}

.moon {
    position: absolute;
    top: 12%;
    right: 15%;
    width: 65px;
    height: 65px;
    border-radius: 50%;
    background: #c9f5ff;
    box-shadow: 0 0 25px #66dfff, 0 0 75px #248bff55;
}

.mountain {
    position: absolute;
    bottom: 50px;
    width: 130%;
    height: 120px;
    left: -10%;
    background: #102540;
    clip-path: polygon(0 100%, 0 80%, 15% 30%, 26% 75%,
        39% 15%, 53% 78%, 67% 35%, 78% 70%,
        90% 20%, 100% 80%, 100% 100%);
    opacity: .9;
}

.mountain.back {
    bottom: 65px;
    transform: translateX(40px) scale(1.1);
    background: #203d5c;
    opacity: .55;
}

.ground {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 55px;
    border-top: 2px solid #4eeaff;
    background: linear-gradient(#142a43, #070c18);
    box-shadow: 0 -5px 25px #16d9ff22;
}

.ground-line {
    position: absolute;
    top: 17px;
    left: 0;
    width: 200%;
    height: 2px;
    background: repeating-linear-gradient(
        90deg, #4eeaff 0 35px, transparent 35px 65px
    );
    opacity: .35;
}

.dino {
    position: absolute;
    left: 11%;
    bottom: 51px;
    width: 49px;
    height: 61px;
    z-index: 3;
    color: #69ffcc;
    filter: drop-shadow(0 0 8px #42ffbd99);
}

.dino svg {
    width: 100%;
    height: 100%;
    overflow: visible;
}

.dino.jumping {
    animation: jump-glow .25s ease-out;
}

@keyframes jump-glow {
    50% { filter: drop-shadow(0 0 18px #4dffe3); }
}

.obstacle {
    position: absolute;
    bottom: 51px;
    z-index: 3;
    color: #ff8a76;
    filter: drop-shadow(0 0 8px #ff4f5677);
}

.cactus {
    width: 28px;
    height: 49px;
}

.bird {
    width: 42px;
    height: 28px;
    color: #ffd27d;
}

.dust {
    position: absolute;
    bottom: 54px;
    left: 13%;
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #72eaff;
    opacity: .6;
    animation: dust 1.3s infinite linear;
}

@keyframes dust {
    from { transform: translateX(0); opacity: .7; }
    to { transform: translateX(-90px) translateY(-15px); opacity: 0; }
}

.overlay {
    position: absolute;
    inset: 0;
    z-index: 5;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    background: #03081685;
    backdrop-filter: blur(3px);
    padding: 20px;
}

.overlay.hidden {
    display: none;
}

.eyebrow {
    color: #70f4ff;
    font-size: 10px;
    letter-spacing: 5px;
    margin-bottom: 12px;
}

.overlay h2 {
    font-size: clamp(26px, 5vw, 48px);
    letter-spacing: 4px;
    text-shadow: 0 0 25px #35dfff55;
}

.overlay p {
    color: #b3c4df;
    font-size: 13px;
    margin-top: 14px;
    line-height: 1.8;
}

.play-btn {
    margin-top: 24px;
    border: 1px solid #65f5ff;
    color: #04101b;
    background: #70f5ff;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 3px;
    padding: 14px 27px;
    border-radius: 4px;
    cursor: pointer;
    box-shadow: 0 0 25px #38dbff44;
    transition: .2s;
}

.play-btn:hover {
    transform: translateY(-2px);
    background: white;
    box-shadow: 0 0 35px #38dbff99;
}

.hud-note {
    position: absolute;
    right: 15px;
    bottom: 13px;
    z-index: 2;
    color: #8ba4c7;
    font-size: 9px;
    letter-spacing: 2px;
}

.bottom {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin-top: 17px;
    flex-wrap: wrap;
}

.controls {
    color: #91a4c5;
    font-size: 11px;
    line-height: 2;
}

kbd {
    display: inline-block;
    border: 1px solid #38516e;
    border-radius: 4px;
    padding: 2px 7px;
    color: #e4faff;
    background: #111e32;
    margin: 0 3px;
}

.difficulty {
    font-size: 10px;
    letter-spacing: 2px;
    color: #72ffcf;
}

@media (max-width: 600px) {
    .game-shell { padding: 12px; }
    .topbar { align-items: flex-start; }
    .status { font-size: 9px; }
    .stats { gap: 20px; }
    .stat-value { font-size: 20px; }
    .moon { width: 45px; height: 45px; }
}
</style>
</head>

<body>
<main class="game-shell">
    <header class="topbar">
        <div>
            <div class="brand">ARCADE SYSTEM / 001</div>
            <h1>NEON RUNNER</h1>
            <div class="subtitle">SURVIVE THE ENDLESS NIGHT</div>
        </div>
        <div class="status">
            SYSTEM STATUS<br><br>
            <span id="status">STANDBY</span>
        </div>
    </header>

    <section class="stats">
        <div>
            <div class="stat-label">SCORE</div>
            <div class="stat-value" id="score">00000</div>
        </div>
        <div>
            <div class="stat-label">BEST</div>
            <div class="stat-value" id="best">00000</div>
        </div>
        <div>
            <div class="stat-label">SPEED</div>
            <div class="stat-value" id="speed">1.0x</div>
        </div>
    </section>

    <section class="game" id="game" aria-label="Dinosaur running game">
        <div class="stars"></div>
        <div class="moon"></div>
        <div class="mountain back"></div>
        <div class="mountain"></div>

        <div class="dino" id="dino">
            <svg viewBox="0 0 50 62" fill="currentColor">
                <path d="M7 22 H20 V9 H37 V17 H44 V31 H36 V42 H28 V56 H20 V43 H13 V56 H5 V34 H0 V26 H7 Z"/>
                <rect x="29" y="12" width="4" height="4" fill="#071323"/>
                <path d="M0 26 H8 V32 H0 Z" fill="#071323"/>
            </svg>
        </div>

        <div class="ground">
            <div class="ground-line" id="groundLine"></div>
        </div>

        <div class="hud-note">SECTOR 01 // NIGHTFALL</div>

        <div class="overlay" id="overlay">
            <div class="eyebrow">THE WORLD IS YOURS</div>
            <h2 id="overlayTitle">READY TO RUN?</h2>
            <p id="overlayText">
                Jump over obstacles. Survive the night.<br>
                How long can you last?
            </p>
            <button class="play-btn" id="playBtn">START MISSION</button>
        </div>
    </section>

    <footer class="bottom">
        <div class="controls">
            <kbd>SPACE</kbd> / <kbd>↑</kbd> JUMP
            &nbsp; <kbd>R</kbd> RESTART
            <br>
            Mobile: tap the game area to jump.
        </div>
        <div class="difficulty" id="difficulty">DIFFICULTY: EASY</div>
    </footer>
</main>

<script>
const game = document.getElementById("game");
const dino = document.getElementById("dino");
const overlay = document.getElementById("overlay");
const playBtn = document.getElementById("playBtn");
const scoreEl = document.getElementById("score");
const bestEl = document.getElementById("best");
const speedEl = document.getElementById("speed");
const statusEl = document.getElementById("status");
const groundLine = document.getElementById("groundLine");
const difficultyEl = document.getElementById("difficulty");
const overlayTitle = document.getElementById("overlayTitle");
const overlayText = document.getElementById("overlayText");

let running = false;
let jumping = false;
let score = 0;
let best = 0;
let speed = 6;
let dinoY = 0;
let velocityY = 0;
let obstacles = [];
let spawnTimer = 0;
let lastTime = 0;
let animationId = null;
let elapsed = 0;
let gameWidth = 0;

const GRAVITY = 0.72;
const JUMP_POWER = 14.5;
const GROUND = 51;

try {
    best = Number(localStorage.getItem("neonRunnerBest")) || 0;
} catch (e) {
    best = 0;
}

bestEl.textContent = String(best).padStart(5, "0");

function createObstacle() {
    const element = document.createElement("div");
    element.className = "obstacle";

    const isBird = score > 250 && Math.random() < 0.25;

    if (isBird) {
        element.classList.add("bird");
        element.innerHTML = `
        <svg viewBox="0 0 45 30" width="100%" height="100%"
             fill="currentColor">
            <path d="M2 18 Q12 2 22 15 Q30 0 43 9
                     L34 20 L22 23 L11 21 Z"/>
            <circle cx="35" cy="11" r="1.5" fill="#10172a"/>
        </svg>`;
        element.style.bottom = (GROUND + 50 + Math.random() * 25) + "px";
    } else {
        element.classList.add("cactus");
        element.innerHTML = `
        <svg viewBox="0 0 30 50" width="100%" height="100%"
             fill="currentColor">
            <path d="M10 49 V18 Q10 10 16 10 Q22 10 22 18
                     V49 H16 V23 H14 V49 Z"/>
            <path d="M10 28 H4 V19 H0 V13 H7 Q13 13 13 20 V28 Z"/>
            <path d="M20 34 H27 V25 H30 V19 H24 Q18 19 18 26 V34 Z"/>
        </svg>`;
        element.style.bottom = GROUND + "px";
    }

    game.appendChild(element);

    obstacles.push({
        el: element,
        x: game.clientWidth + 20,
        width: isBird ? 38 : 27,
        height: isBird ? 24 : 43,
        isBird: isBird,
        bottom: parseFloat(element.style.bottom)
    });
}

function startGame() {
    if (animationId) cancelAnimationFrame(animationId);

    obstacles.forEach(o => o.el.remove());
    obstacles = [];

    score = 0;
    speed = 6;
    dinoY = 0;
    velocityY = 0;
    jumping = false;
    spawnTimer = 0;
    elapsed = 0;
    lastTime = 0;
    gameWidth = game.clientWidth;

    dino.style.bottom = GROUND + "px";
    dino.classList.remove("jumping");

    scoreEl.textContent = "00000";
    speedEl.textContent = "1.0x";
    difficultyEl.textContent = "DIFFICULTY: EASY";

    overlay.classList.add("hidden");
    statusEl.textContent = "RUNNING";
    statusEl.style.color = "#67ffca";

    running = true;
    animationId = requestAnimationFrame(loop);
}

function jump() {
    if (!running) return;

    if (!jumping) {
        jumping = true;
        velocityY = JUMP_POWER;
        dino.classList.add("jumping");

        setTimeout(() => {
            dino.classList.remove("jumping");
        }, 250);
    }
}

function endGame() {
    running = false;
    statusEl.textContent = "GAME OVER";
    statusEl.style.color = "#ff8585";

    if (score > best) {
        best = score;
        bestEl.textContent = String(best).padStart(5, "0");
        try {
            localStorage.setItem("neonRunnerBest", String(best));
        } catch (e) {}
    }

    overlayTitle.textContent = "MISSION FAILED";
    overlayText.innerHTML =
        "FINAL SCORE: <strong>" + score +
        "</strong><br>Every run makes you stronger. Try again!";

    playBtn.textContent = "RETRY MISSION";
    overlay.classList.remove("hidden");
}

function loop(timestamp) {
    if (!running) return;

    if (!lastTime) lastTime = timestamp;
    const dt = Math.min((timestamp - lastTime) / 16.667, 2);
    lastTime = timestamp;

    elapsed += dt;
    gameWidth = game.clientWidth;

    score += Math.floor(dt * speed / 6);
    speed = Math.min(6 + score / 180, 15);

    scoreEl.textContent = String(score).padStart(5, "0");
    speedEl.textContent = (speed / 6).toFixed(1) + "x";

    if (score > 1000) {
        difficultyEl.textContent = "DIFFICULTY: EXTREME";
    } else if (score > 400) {
        difficultyEl.textContent = "DIFFICULTY: HARD";
    } else if (score > 150) {
        difficultyEl.textContent = "DIFFICULTY: MEDIUM";
    }

    groundLine.style.transform =
        "translateX(-" + ((elapsed * speed * 2) % 65) + "px)";

    if (jumping) {
        dinoY += velocityY * dt;
        velocityY -= GRAVITY * dt;

        if (dinoY <= 0) {
            dinoY = 0;
            velocityY = 0;
            jumping = false;
        }

        dino.style.bottom = (GROUND + dinoY) + "px";
    }

    spawnTimer -= dt;

    if (spawnTimer <= 0) {
        createObstacle();
        spawnTimer = Math.max(42, 90 - speed * 2) +
                     Math.random() * 35;
    }

    const dinoRect = {
        left: dino.offsetLeft + 7,
        right: dino.offsetLeft + dino.offsetWidth - 5,
        top: game.clientHeight - GROUND - dinoY -
             dino.offsetHeight + 7,
        bottom: game.clientHeight - GROUND - dinoY - 5
    };

    for (let i = obstacles.length - 1; i >= 0; i--) {
        const o = obstacles[i];
        o.x -= speed * dt;
        o.el.style.left = o.x + "px";

        const top = game.clientHeight - o.bottom - o.height;

        const hit = (
            dinoRect.right > o.x + 5 &&
            dinoRect.left < o.x + o.width - 4 &&
            dinoRect.bottom > top + 3 &&
            dinoRect.top < top + o.height - 3
        );

        if (hit) {
            endGame();
            return;
        }

        if (o.x < -70) {
            o.el.remove();
            obstacles.splice(i, 1);
        }
    }

    animationId = requestAnimationFrame(loop);
}

playBtn.addEventListener("click", startGame);

game.addEventListener("pointerdown", function(e) {
    if (e.target === playBtn) return;

    if (!running) {
        startGame();
    } else {
        jump();
    }
});

document.addEventListener("keydown", function(e) {
    if (["Space", "ArrowUp"].includes(e.code)) {
        e.preventDefault();

        if (!running) {
            startGame();
        } else {
            jump();
        }
    }

    if (e.code === "KeyR") {
        startGame();
    }
});

document.addEventListener("visibilitychange", function() {
    if (document.hidden && running) {
        statusEl.textContent = "PAUSED";
    } else if (running) {
        statusEl.textContent = "RUNNING";
    }
});
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
