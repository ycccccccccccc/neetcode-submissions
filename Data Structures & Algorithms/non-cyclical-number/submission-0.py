class Solution:
    def isHappy(self, n: int) -> bool:
        existed = set()
        while True:
            if n in existed: return False
            if n == 1: return True
            existed.add(n)
            temp = n
            n = 0
            while temp > 0:
                n += (temp%10) ** 2
                temp = temp // 10
        