var numbers = [1, 400, 12, 34, 5, 10000];
var i = 0;
var total = 0;
while(i < numbers.length) {
    total = total + numbers[i];
    i++;
}
console.log(`total: ${total}`);