class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def backtrack(l: int, r: int, p: str):
            if len(p) == n*2:
                res.append(p)
            if l < r:
                backtrack(l, r-1, p+")")
            if l > 0:
                backtrack(l-1, r, p+"(")

        backtrack(n-1, n, "(")   
        return res