class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int temp = 0;
        int pemt = numbers.size() - 1;
        vector<int> v;
        for (int u = 0; u < numbers.size(); u++) {
            if (numbers[temp] + numbers[pemt] < target) {
                temp += 1;
            }
            else if (numbers[temp] + numbers[pemt] > target) {
                pemt -= 1;
            }
            else {
                v.push_back(temp+1);
                v.push_back(pemt+1);
                return v;
            }
        }
    }
};
