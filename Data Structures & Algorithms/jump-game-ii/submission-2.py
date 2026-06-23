class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums)] * len(nums)
        dp[0] = 0
        minStep = len(nums)
        for i in range(len(nums)):
            minStep = min(dp[i], minStep)
            nextIndex = i+nums[i] if i + nums[i] < len(nums) else -1
            dp[nextIndex] = min(dp[nextIndex], minStep + 1)
            minStep += 1
        return dp[-1]