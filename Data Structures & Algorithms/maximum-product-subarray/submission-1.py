class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        max_dp = max(0, nums[0])
        min_dp = min(0, nums[0])

        ans = max_dp
        for i in range(1, len(nums)):
            max_dp_t = max([nums[i], max_dp*nums[i], min_dp*nums[i]])
            min_dp = min([nums[i], max_dp*nums[i], min_dp*nums[i]])
            max_dp = max_dp_t

            ans = max(ans, max_dp)

        return ans


