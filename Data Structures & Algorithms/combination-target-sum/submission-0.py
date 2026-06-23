class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        numsSet = []
        numsLength = len(nums)

        def getSum(newNums: List[int], index: int, target: int) -> None:
            nonlocal numsLength, nums
            if target == 0:
                numsSet.append(newNums)
                return
            
            if target < 0 or index >= numsLength:
                return
            
            getSum(newNums + [nums[index]], index, target-nums[index])
            getSum(newNums, index+1, target)

        getSum([], 0, target)
        return numsSet