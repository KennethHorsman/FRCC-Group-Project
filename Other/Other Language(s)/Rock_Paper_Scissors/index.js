let userScore = 0;
let computerScore = 0;
let userScore_span = document.getElementById("user-score");
let computerScore_span = document.getElementById("comp-score");
const scoreBoard_div = document.querySelector(".score-board");
let result_div = document.getElementById("result");
const rock_div = document.getElementById("rock");
const paper_div = document.getElementById("paper");
const scissors_div = document.getElementById("scissors");

function getCompChoice() {
    const choices = ["rock", "paper", "scissors"];
    const randomNum = Math.floor(Math.random() * 3);
    return choices[randomNum];
}

function win(user_choice, comp_choice) {
    userScore++;
    userScore_span.innerHTML = userScore;
    result_div.innerHTML = user_choice + " beats " + comp_choice + ". You win!";
    document.getElementById(user_choice).classList.add("green-glow");
    setTimeout(function() { document.getElementById(user_choice).classList.remove("green-glow");}, 1000);
    console.log(user_choice, userScore);
    console.log(comp_choice, computerScore);
}
function lose(user_choice, comp_choice) {
    computerScore++;
    computerScore_span.innerHTML = computerScore;
    result_div.innerHTML = comp_choice + " loses to " + user_choice + ". You lose!";
    document.getElementById(user_choice).classList.add("red-glow");
    setTimeout(function () { document.getElementById(user_choice).classList.remove("red-glow"); }, 1000);
    console.log(user_choice, userScore);
    console.log(comp_choice, computerScore);
}
function draw(user_choice, comp_choice) {
    result_div.innerHTML = comp_choice + " is the same as " + user_choice + ". It's a draw!";
    document.getElementById(user_choice).classList.add("gray-glow");
    setTimeout(function () { document.getElementById(user_choice).classList.remove("gray-glow"); }, 1000);
    console.log(user_choice, userScore);
    console.log(comp_choice, computerScore);
}

function game(userChoice) {
    const computerChoice = getCompChoice();
    switch (userChoice + computerChoice) {
        case "rockscissors":
        case "paperrock":
        case "scissorspaper":
            win(userChoice, computerChoice);
            break;
        case "rockpaper":
        case "paperscissors":
        case "scissorsrock":
            lose(userChoice, computerChoice);
            break;
        case "rockrock":
        case "paperpaper":
        case "scissorsscissors":
            draw(userChoice, computerChoice);
            break;
    }
}

function main() {
    rock_div.addEventListener("click", function() {
        game("rock");
    });

    paper_div.addEventListener("click", function () {
        game("paper");
    });

    scissors_div.addEventListener("click", function () {
        game("scissors");
    });
}

main();