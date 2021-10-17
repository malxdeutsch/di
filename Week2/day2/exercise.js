let x = 5;
let y = 2;
if (x>y) {
    console.log("x is the bigger number");
}
else {
    console.log("y is the bigger number");
}

let newDog = "Chihuahua"
console.log(newDog.length);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

if (newDog == "Chihuahua") {
    console.log("I love Chihuahuas, it’s my favorite dog breed");
}
else {
    console.log("I dont care, I prefer cats");
}


let q = prompt("Give a number.")
if (q%2 == 0) {
    console.log(`${q} is an even number`);
}
else {
    console.log(`${q} is an odd number`);
}


let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let userName= users[0]
let length = users.length - 2

if (users = 0) {
    console.log("No one is online.");
}
else if (users = 1) {
    console.log(`${userName} is online`);
} else if (users = 2){
    console.log(`${userName[0]} and ${userName[1]} are online`);
}
else{
    console.log(`${userName[0]} and ${userName[1]} and ${lengtg} users are online`);
}
