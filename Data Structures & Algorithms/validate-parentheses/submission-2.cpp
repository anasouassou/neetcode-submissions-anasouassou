class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char>closeToOpen = {{'}', '{'}, {')' , '('}, 
        {']', '['}};
        stack<char> ss;
        for (char u : s) {
            if (!closeToOpen.count(u)) ss.push(u);
            else {
                if (!ss.empty() && ss.top() == closeToOpen[u]) ss.pop();
                else return false ;
            }
        }
        return ss.empty();
    }
};
