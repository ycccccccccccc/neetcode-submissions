class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subNums = set()

        def getSubsets(originNums: List[int], index: int, numsLength: int) -> None:
            nonlocal subNums
            subNums.add(originNums)
            newNums = originNums + (nums[index],)
            subNums.add(newNums)
            
            if index+1 < numsLength:
                getSubsets(originNums, index+1, numsLength)
                getSubsets(newNums, index+1, numsLength)

        
        getSubsets((), 0, len(nums))
        return [list(t) for t in subNums]