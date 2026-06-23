class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]: return nums[0]
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            m = (l+r)//2
            if m+1 < n and nums[m+1] < nums[m]:
                return nums[m+1]
            if nums[m] > nums[l]:
                l = m + 1
            else:
                r = m - 1

        return nums[l+2]