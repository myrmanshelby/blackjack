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

ten.addEventListener('click', async () => {
    const isValid = await checkValidBet(10)
    if(isValid){
        bet+=10
        betTracker.textContent = "Current Bet: "+String(bet)
        subtractBet(10)
    }
})

fifty.addEventListener('click', async () => {
    const isValid = await checkValidBet(50)
    if(isValid){
        bet+=50
        betTracker.textContent = "Current Bet: "+String(bet)
        subtractBet(50)
    }

})

hundred.addEventListener('click', async () => {
    const isValid = await checkValidBet(100)
    if(isValid){
        bet+=100
        betTracker.textContent = "Current Bet: "+String(bet)
        subtractBet(100)
    }
})

fiveH.addEventListener('click', async () => {
    const isValid = await checkValidBet(500)
    if(isValid){
        bet+=500
        betTracker.textContent = "Current Bet: "+String(bet)
        subtractBet(500)
    }
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

async function checkValidBet(betVal) {
    let currentChips;
    try {
        const response = await fetch('/chip_total');
        const data = await response.json();
        currentChips = data.chip_total
    } catch {
        console.error('Error fetching chip total: ', error);
        return false
    }
    if(currentChips>=betVal) {
        return true;
    } else {
        return false;
    }
}

// TO DO: fetch initial deal once player hits start round

const hit = document.createElement("button");
hit.textContent = "Hit"
const stay = document.createElement("button");
stay.textContent = "Stay"

startRound.addEventListener('click', () => {
    buttons.removeChild(ten);
    buttons.removeChild(fifty);
    buttons.removeChild(hundred);
    buttons.removeChild(fiveH);
    
    buttons.appendChild(hit)
    buttons.appendChild(stay)

    controls.removeChild(startRound)
    fetch('/first_deal')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            add_card_player(data.p_card_one)
            add_card_player(data.p_card_two)
            add_card_dealer(data.d_card_one)
            add_card_dealer(data.d_card_two)
        })
})

async function add_card_player(cardName) {
    const playerHand = document.querySelector('.player-hand')
    const img = document.createElement("img");
    img.src = cardUrls[cardName];
    playerHand.appendChild(img);
}

async function add_card_dealer(cardName) {
    const dealerHand = document.querySelector('.dealer-hand')
    const img = document.createElement("img");
    img.src = cardUrls[cardName];
    dealerHand.appendChild(img);
}