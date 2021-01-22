class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_at = [0] * len(nums)
        max_sum_at[0] = nums[0]
        for i in range(1, len(nums)):
            max_sum_at[i] = max(nums[i], nums[i] + max_sum_at[i - 1])
        return(max(max_sum_at))
        
