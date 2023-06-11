// https://leetcode.com/problems/majority-element/

// it's in C++ because i was mad that the optimal python solution
// is to sort the fucking list and split it in half because python's
// sort functions are implemented in C or something and the runtime
// graph is just going to live in my head rent free for what
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int element = nums[0];
        unsigned short counter = 1;
        for (unsigned short i = 1; i < nums.size(); ++i) {
            counter += 2 * (nums[i] == element) - 1 ;
            if (counter == 0) {
                element = nums[i];
                counter = 1;
            }
        }
        return element;
    }
};
