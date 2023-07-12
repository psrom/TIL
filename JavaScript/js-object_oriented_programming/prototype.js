function Person(name, first, second, third){
    this.name=name;
    this.first=first;
    this.second=second;
    this.third=third;
}

Person.prototype.sum = function(){
    return 'prototype: '+(this.first+this.second);
}

// 객체 자신의 sum function을 가지고 있는지 먼저 확인
var kim = new Person('kim', 10, 20);
kim.sum = function(){
    return 'this: '+(this.first+this.second);
}
console.log("kim.sum()", kim.sum());

// lee 객체는 자신만의 sum이 없기 때문에 Person.prototype.sum을 불러옴
var lee = new Person('lee', 10, 10);
console.log("lee.sum()", lee.sum());
