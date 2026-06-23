class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        max_dp = [0] * len(nums)
        min_dp = [0] * len(nums)
        max_dp[0] = max(0, nums[0])
        min_dp[0] = min(0, nums[0])

        ans = max_dp[0]
        for i in range(1, len(nums)):
            max_dp[i] = max([nums[i], max_dp[i-1]*nums[i], min_dp[i-1]*nums[i]])
            min_dp[i] = min([nums[i], max_dp[i-1]*nums[i], min_dp[i-1]*nums[i]])

            ans = max(ans, max_dp[i])

        return ans


