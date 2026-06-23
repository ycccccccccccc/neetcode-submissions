class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        found = False
        target = sum(nums)
        if target % 2: return False

        target //= 2

        def findPartition(newSum: int, index: int) -> None:
            nonlocal found
            if newSum > target or index >= len(nums): return
            if newSum == target:
                found = True
                return
            findPartition(newSum + nums[index], index + 1)
            findPartition(newSum, index + 1)

        findPartition(0, 0)
        return found
