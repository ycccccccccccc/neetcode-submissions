class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxPosition = nums[0]

        for i in range(1, len(nums)):
            if maxPosition < i:
                return False
            maxPosition = max(maxPosition, i + nums[i])

        return True