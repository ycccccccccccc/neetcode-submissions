class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        
        def robInRange(l: int, r: int) -> int:
            prev1, prev2 = nums[l], nums[l+1]
            maxRob = 0
            for i in range(l+2, r):
                prev1, prev2 = max(prev1, prev2), max(prev1+nums[i], prev2)
            return prev2

        return max(robInRange(0, len(nums)-1), robInRange(1, len(nums)))