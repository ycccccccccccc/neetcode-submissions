class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits)-1, 0, -1):
            if digits[i] > 9:
                digits[i-1] += 1
                digits[i] -= 10
            else:
                break
        if digits[0] > 9: return [1, digits[0]%10] + digits[1:]
        return digits