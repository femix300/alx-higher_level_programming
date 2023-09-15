#!/usr/bin/node

exports.logMe = function (item) {
    if (typeof exports.logMe.noOfCalls === 'undefined') {
        exports.logMe.noOfCalls = 0;
    }
    
    console.log(exports.logMe.noOfCalls, ": ", item);
    exports.logMe.noOfCalls++;
}