class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[-1]
        dp = nums
        dp[1] = max(nums[:2])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[-1]