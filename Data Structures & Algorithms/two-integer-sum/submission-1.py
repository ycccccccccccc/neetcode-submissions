class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_note = dict()
        for i, num in enumerate(nums):
            if target - num in index_note:
                return [index_note[target-num], i]
            index_note[num] = i