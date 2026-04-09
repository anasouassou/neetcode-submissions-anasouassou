class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size();
        while (l < r) {
            int middle = l + (r - l) / 2;
            if (nums[middle] >= target) r = middle;
            else l = middle + 1;
        }
        return (l < nums.size() && nums[l] == target) ? l : -1;
    }
};
