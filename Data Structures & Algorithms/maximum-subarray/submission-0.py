class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        past_sum = max_sum = nums[0]

        for num in nums[1:]:
            past_sum = max(past_sum, 0)
            past_sum += num

            max_sum = max(past_sum, max_sum)

        return max_sum