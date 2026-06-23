class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        start = l
        l, r = 0, n-1
        if target > nums[(start-1)%n] or target < nums[start]:
            return -1
        if target <= nums[-1]:
            l = start
        else:
            r = (start-1)%n

        while l <= r:
            m = (l+r)//2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1

