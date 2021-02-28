// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/submissions/

class Solution {
public:
    string removeDuplicates(string S) {
        std::string s;
        for (int i = 0; i < S.length(); ++i) {
            if (s.length() > 0 && S[i] == s.back()) {
                s.pop_back();
            }
            else {
                s.push_back(S[i]);
            }
        }
        return s;
    }
};
