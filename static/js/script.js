const ten = document.createElement("button");
ten.textContent = "10"
const fifty = document.createElement("button");
fifty.textContent = "50"
const hundred = document.createElement("button");
hundred.textContent = "100"
const fiveH = document.createElement("button");
fiveH.textContent = "500"
const startRound = document.createElement("button");
startRound.textContent = "Start Round"

const buttons = document.querySelector(".buttons");
const controls = document.querySelector(".controls");

const ctrlContainer = document.querySelector(".ctrl-container")
const betTracker = document.createElement("div");
betTracker.textContent = "Current bet: 0"

const startGame = document.getElementById("start-game")
startGame.addEventListener('click', () => {
    buttons.removeChild(startGame)

    buttons.appendChild(ten)
    buttons.appendChild(fifty)
    buttons.appendChild(hundred)
    buttons.appendChild(fiveH)

    controls.appendChild(startRound)
    ctrlContainer.appendChild(betTracker)
})