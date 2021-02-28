// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/submissions/

#include <stack>

class Solution {
public:
    string removeDuplicates(string S) {
        std::stack<char> s;
        std::string res = "";
        for (int i = S.length() - 1; i >= 0; --i) {
            if (s.size() > 0 && S[i] == s.top()) {
                s.pop();
            }
            else {
                s.push(S[i]);
            }
        }
        while (!s.empty()) {
            res += s.top();
            s.pop();
        }
        return res;
    }
};
