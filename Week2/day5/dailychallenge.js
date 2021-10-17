let question = prompt("Give a number to begin counting the bottles of beer.")

function beerBottles(){
 let beer = 0
do {
    beer ++
    if(question <= beer){
console.log(`${question} bottle of beer on the wall \n ${question} bottle of beer \n take ${question} town and pass it around`);
    }
     else {
     console.log(`${question} of bottles of beer on the wall \n ${question} of bottles of beer \n take ${beer} down, pass them around`);
     }   
     question = question - beer
}
while (question >= beer) 

console.log("0 bottles of beer on the wall");
}

beerBottles()