class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        for (int u = 0; u < nums.size(); u++) {
            if (mp.find(target - nums[u]) != mp.end()) {
                return {mp[target - nums[u]], u};
            }
            mp.insert({nums[u], u});
        }
    }
};
