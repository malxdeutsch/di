

function playTheGame() {
    let answer = confirm("Do you want to play the game?")
    if (answer == false) {
        alert("No problem, Goodbye.");
    }
    else {
        let game = parseInt(prompt("Enter a number between 1 and 10."))
        if (isNaN(game)) {
        alert("Sorry, not a number, Goodbye.")
    }
        else if (game < 0 || game > 10){
        alert("Sorry, it’s not a good number, Goodbye.")
    }
         else {
        let computer = Math.floor(Math.random() * 11);
        test(game,computer)
    }

}
}

function test(userNumber,computerNumber) {
    let counter=1
    console.log(userNumber,computerNumber);
    do{
    if (userNumber == computerNumber){
        alert("Winner!");
        break;
    }
    else if (userNumber > computerNumber){
        userNumber=prompt("Your number is bigger then the computer’s. Guess again")
       counter++
    }
    else if (userNumber < computerNumber) {
        userNumber=prompt("Your number is smaller then the computer’s. Guess again")
        counter++
    }
    if ( counter > 2) {
        alert("Out of chances.")
        break;
    }
}while(userNumber !== computerNumber);
}


playTheGame()
