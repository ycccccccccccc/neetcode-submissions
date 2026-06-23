class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_pro = 1
        has_zero = False
        has_zeros = False
        for num in nums:
            if num != 0:
                all_pro *= num
            else:
                if has_zero:
                    has_zeros = True
                has_zero = True
        if has_zeros:
            return [0 for _ in range(len(nums))]
        if has_zero:
            return [all_pro if num == 0 else 0 for num in nums]
        return [all_pro//num for num in nums]