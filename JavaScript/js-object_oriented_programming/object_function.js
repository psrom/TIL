var kim = {name:'kim', first:10, second:20}
var lee = {name:'lee', first:10, second:10}
function sum(prefix){
    return prefix + (this.first + this.second);
}
// sum();

console.log("sum.call(kim)", sum.call(kim, '=>')); // .call() 함수 내의 this를 바꾼다
console.log("sum.call(lee)", sum.call(lee, ': '));
var kimSum = sum.bind(kim, '->'); // .bind 새로운 함수를 만든다
console.log("kimSum() ", kimSum());

