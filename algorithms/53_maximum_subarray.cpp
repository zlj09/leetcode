class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> max_sum_at(n);
        max_sum_at[0] = nums[0];
        int max_sum = nums[0];
        for (int i = 1; i < n; i++) {
            max_sum_at[i] = (max_sum_at[i - 1] >= 0) ? (nums[i] + max_sum_at[i - 1]) : (nums[i]);
            max_sum = (max_sum < max_sum_at[i]) ? (max_sum_at[i]) : max_sum;
        }
        return(max_sum);
    }
};
