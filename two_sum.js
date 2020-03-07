// 1. Two Sum
// Given an array of integers, return indices of the two numbers such that they 
// add up to a specific target.

// You may assume that each input would have exactly one solution, and you may 
// not use the same element twice.
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    var res = [];
    for (var i = 0; i < nums.length - 1; i = i + 1) {
        for (var j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                res.push(i);
                res.push(j);
                return res;
            }
        }
    }
    return res;
};
