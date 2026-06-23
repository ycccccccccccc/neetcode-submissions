class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        isPositive = True if n > 0 else False
        n = abs(n)

        n_bin = bin(n)[2:]
        base = x
        res = 1
        
        for i in range(len(n_bin)-1, -1, -1):
            res *= base if n_bin[i] == "1" else 1
            base **= 2
    
        return res if isPositive else 1/res