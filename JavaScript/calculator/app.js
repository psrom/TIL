const calculator = {
    plus: function(a, b){
        return a + b;
    },
    minus: function(a, b){
        return a - b;
    },
    divide: function(a, b){
        if (b == 0){
            return "b cannot be 0";
        } else{
            return a / b;
        }
    },
    times: function(a, b){
        return a * b;
    },
    power: function(a, b){
        return a ** b;
    }
};

const plusResult = calculator.plus(2, 3);
const minusResult = calculator.minus(plusResult, 10);
const timesResult = calculator.times(10, minusResult);
const divideResult = calculator.divide(timesResult, plusResult);
const powerResult =  calculator.power(divideResult, minusResult);
