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
betTracker.textContent = "Current bet: 0";
const chipTotal = document.createElement("div");
betTracker.classList.add("bet-tracker")
chipTotal.classList.add("bet-tracker")

let bet = 0;

const startGame = document.getElementById("start-game")
startGame.addEventListener('click', () => {
    buttons.removeChild(startGame);

    buttons.appendChild(ten);
    buttons.appendChild(fifty);
    buttons.appendChild(hundred);
    buttons.appendChild(fiveH);

    fetch('/chip_total')
        .then(response => response.json())
        .then(data => {
            chipTotal.textContent=`Current Chip Total: ${data.chip_total}`
        })
    controls.appendChild(startRound);
    controls.appendChild(chipTotal)
    controls.appendChild(betTracker);
})

ten.addEventListener('click', () => {
    bet+=10
    betTracker.textContent = "Current Bet: "+String(bet)
    subtractBet(10)
})

fifty.addEventListener('click', () => {
    bet+=50
    betTracker.textContent = "Current Bet: "+String(bet)
    subtractBet(50)

})

hundred.addEventListener('click', () => {
    bet+=100
    betTracker.textContent = "Current Bet: "+String(bet)
    subtractBet(100)
})

fiveH.addEventListener('click', () => {
    bet+=500
    betTracker.textContent = "Current Bet: "+String(bet)
    subtractBet(500)
})

function subtractBet(betVal) {
    fetch('/subtract_bet', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({value: betVal})
    }).then(response=>response.json())
    .then(data=> {
        chipTotal.textContent=`Current Chip Total: ${data.chip_total}`
    })
}