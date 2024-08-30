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
            chips = data.chipTotal
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

function addBet(betVal) {
    fetch('/add_bet', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({value: betVal})
    }).then(response=>response.json())
    .then(data=> {
        console.log(data.chip_total)
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

startRound.addEventListener('click', async () => {
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
            addCardPlayer(data.p_card_one)
            addCardPlayer(data.p_card_two)
            addCardDealer(data.d_card_one)
            addCardDealer(data.d_card_two)
        })

    fetch('/check_natural')
        .then(response => response.json())
        .then(data => {
            setTimeout(async () => {
                if(data.natural!='none'){
                    scores = await getScores()
                    if(data.natural==='player'){
                        showPopup('player-natural', scores[0], scores[1])
                    } else if(data.natural==='dealer'){
                        showPopup('dealer-natural', scores[0], scores[1])
                    } else if(data.natural==='both'){
                        showPopup('both-natural', scores[0], scores[1])
                    }
                }
            }, 750)
        })
})

async function getScores(){
    let dealerScore
    let playerScore
    try {
        const playerResponse = await fetch('/player_score');
        const playerData = await playerResponse.json();
        playerScore = playerData.player_score;

        const dealerResponse = await fetch('/dealer_score');
        const dealerData = await dealerResponse.json();
        dealerScore = dealerData.dealer_score;

        return [playerScore, dealerScore];
    } catch (error) {
        console.error('Error fetching scores:', error);
    }
}

async function getDealerScore(){
    let dealerScore
    try {
        const dealerResponse = await fetch('/dealer_score');
        const dealerData = await dealerResponse.json();
        dealerScore = dealerData.dealer_score;

        return dealerScore;
    } catch (error) {
        console.error('Error fetching scores:', error);
    }
}

hit.addEventListener('click', async () => {
    fetch('/hit')
        .then(response => response.json())
        .then(data => {
            addCardPlayer(data.new_card);
        })

    setTimeout(async () => {
        scores = await getScores()
        if (scores[0]>21){
            flipCardDealer();
            await new Promise(resolve => setTimeout(resolve, 750));
            showPopup('bust', scores[0], scores[1]);
        }
    }, 750)
})

stay.addEventListener('click', async () => {
    flipCardDealer();
    
    let dealerScore=await getDealerScore()
    await dealerPlay(dealerScore)

    setTimeout(async () => {
        scores = await getScores();
        let popupType = ''
        if (scores[1]>21){
            popupType='dealer-bust'
            addBet(bet*2)
        } else if (scores[0]>scores[1]) {
            popupType='player-win'
            addBet(bet*2)
        } else if (scores[1]>scores[0]) {
            popupType='player-lose'
        } else {
            popupType='tie'
            addBet(bet)
        }

        showPopup(popupType, scores[0], scores[1]);
    }, 750)
})

async function dealerPlay(dealerScore) {
    if(dealerScore<=16){
        await new Promise(resolve => setTimeout(resolve, 750));

        try {
            const response = await fetch('/hit_dealer');
            const data = await response.json();
            addCardDealer(data.new_card);
        } catch (error) {
            console.error('Error fetching new dealer card: ', error);
        }

        dealerScore = await getDealerScore();
        console.log(dealerScore)

        await dealerPlay(dealerScore);
    }
}

async function addCardPlayer(cardName) {
    const playerHand = document.querySelector('.player-hand')
    const img = document.createElement("img");
    img.src = cardUrls[cardName];
    img.classList.add('player-'+cardName);
    playerHand.appendChild(img);
}

async function addCardDealer(cardName) {
    const dealerHand = document.querySelector('.dealer-hand')
    const img = document.createElement("img");
    img.src = cardUrls[cardName];
    img.classList.add('dealer-'+cardName);
    dealerHand.appendChild(img);
}

async function flipCardDealer() {
    const dealerHand = document.querySelector('.dealer-hand');
    const img = document.querySelector('.dealer-card_back');
    dealerHand.removeChild(img);

    let flipped_card;
    try {
        const response = await fetch('/flip_card_dealer');
        const data = await response.json();
        flipped_card = data.card
    } catch {
        console.error('Error fetching flipped card value: ', error);
    }

    addCardDealer(flipped_card)
}

function showPopup(popupType, playerScore, dealerScore) {
    const popupContainer = document.querySelector('.popup-container')
    const popup = document.querySelector('.popup')
    popupContainer.style.display = 'flex';
    popup.style.visibility = 'visible';
    const header = document.querySelector('.popup-header')
    const message = document.querySelector('.message')
    const winnerMessage = document.querySelector('.winner-message')
    const player = document.querySelector('.player-score')
    const dealer = document.querySelector('.dealer-score')
    player.textContent=`Player Score: ${playerScore}`
    dealer.textContent=`Dealer Score: ${dealerScore}`

    if (popupType==='bust') {
        header.textContent = 'Bust!'
        message.textContent = "Your score went higher than 21. That's a bust!"
        winnerMessage.textContent = "The dealer wins this round."
    } else if(popupType==='player-natural') {
        header.textContent = "You're a Natural!"
        message.textContent = "You scored 21 on the first deal."
        winnerMessage.textContent = "You win this round!"
    } else if(popupType==='dealer-natural') {
        header.textContent = "The Dealer's a Natural!"
        message.textContent = "The dealer scored 21 on the first deal."
        winnerMessage.textContent = "The dealer wins this round!"
    } else if(popupType==='both-natural') {
        header.textContent = "It's a Tie!"
        message.textContent = "You and the dealer both got a natural"
        winnerMessage.textContent = "You get your bet back!"
    } else if(popupType==='player-win') {
        header.textContent = "You Win!"
        message.textContent = "Your score is higher than the dealer's."
        winnerMessage.textContent = "You win this round!"
    } else if(popupType==='player-lose') {
        header.textContent = "You Lose!"
        message.textContent = "Your score is lower than the dealer's."
        winnerMessage.textContent = "The dealer wins this round!"
    } else if(popupType==='dealer-bust') {
        header.textContent = "You Win!"
        message.textContent = "The dealer's score went higher than 21. That's a bust!"
        winnerMessage.textContent = "You win this round!"
    } else if(popupType==='tie') {
        header.textContent = "It's a Tie"
        message.textContent = "You and the dealer have the same score."
        winnerMessage.textContent = "You get your bet back!"
    }
}