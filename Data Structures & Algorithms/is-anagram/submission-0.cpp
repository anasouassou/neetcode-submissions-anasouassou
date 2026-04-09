class Solution {
public:
    bool isAnagram(string s, string t) {
        multiset<char> ss(s.begin(), s.end());
        multiset<char> tt(t.begin(), t.end());
        if (ss == tt) return 1;
        return 0;

    }
};
