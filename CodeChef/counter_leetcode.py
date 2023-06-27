/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    my_counter = 0
    return function() {
        my_counter++;
        return n + my_counter - 1;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */