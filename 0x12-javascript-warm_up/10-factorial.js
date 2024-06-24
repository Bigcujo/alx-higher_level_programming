#!/usr/bin/node
const nums = process.argv[2];
function factorials (nums) {
    if (isNaN(nums) || nums === 1){
        return (1);
    } else {
        return (nums * factorials(nums - 1));
    }
}
console.log(factorials(parseInt(nums)));
