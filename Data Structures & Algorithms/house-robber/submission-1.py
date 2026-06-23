class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[-1]
        dp = [0] + nums
        for i in range(3, len(nums)+1):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i-1]

        return max(dp[-1], dp[-2])