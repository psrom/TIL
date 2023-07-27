const calculator = {
    add: function(a, b){
        console.log(a + b);
    },
    minus: function(a, b){
        console.log(a - b);
    },
    divide: function(a, b){
        if (b == 0){
            console.log("b cannot be 0");
        } else{
            console.log(a/b);
        }
    },
    powerof: function(a, b){
        console.log(a ** b);
    }
};