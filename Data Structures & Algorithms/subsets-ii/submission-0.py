class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        numsLen = len(nums)
        nums.sort()

        res = []

        def findSubsets(newNums: List[int], index: int) -> None:
            res.append(newNums.copy())
            for i in range(index, numsLen):
                if i > index and nums[i] == nums[i-1]:
                    continue
                newNums.append(nums[i])
                findSubsets(newNums, i+1)
                newNums.pop()

        findSubsets([], 0)
        return res