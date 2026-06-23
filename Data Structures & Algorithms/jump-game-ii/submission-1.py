class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums)] * len(nums)
        dp[0] = 0
        minStep = len(nums)
        for i in range(len(nums)):
            minStep = min(dp[i], minStep)
            if i + nums[i] < len(nums):
                dp[i+nums[i]] = min(dp[i+nums[i]], minStep + 1)
            else:
                dp[-1] = min(dp[-1], minStep + 1)
            minStep += 1
        return dp[-1]