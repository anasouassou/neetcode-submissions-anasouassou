#include <algorithm>
#include <cctype>

class Solution {
public:
    bool isPalindrome(string s) {
        string filtered;
        for (auto it = s.begin(); it < s.end(); it++) {
            if (isalnum(*it)) {
                filtered += tolower(*it);
            }
        }
        for (int u = 0; u < filtered.length(); u++) {
            if (filtered[u] != filtered[filtered.length()-u-1]) return false;
        }
        return true;
    }
};

