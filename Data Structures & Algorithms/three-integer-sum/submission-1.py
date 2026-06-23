class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_c = Counter(nums)
        tri = []

        n = len(nums)
        for i in range(n):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue

            nums_c[nums[i]] -= 1
            for j in range(i+1, n):
                if j != i+1 and nums[j] == nums[j-1]: continue
                num_k = -(nums[i] + nums[j])
                if num_k < nums[j]: continue
                nums_c[nums[j]] -= 1
                if num_k in nums_c and nums_c[num_k] > 0:
                    tri.append([nums[i], nums[j], num_k])
                nums_c[nums[j]] += 1
            nums_c[nums[i]] += 1

        return list(tri)