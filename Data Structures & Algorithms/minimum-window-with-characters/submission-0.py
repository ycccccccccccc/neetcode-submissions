class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        c = Counter(t)

        res = s
        not_exist = len(c)
        l = 0
        for r in range(len(s)):
            c[s[r]] = c.get(s[r], 0) - 1
            if c[s[r]] == 0: 
                not_exist -= 1
            while not_exist == 0 and c[s[l]] < 0:
                c[s[l]] += 1
                l += 1
            if not_exist == 0 and len(res) > (r-l+1):
                res = s[l:r+1]
        if not_exist > 0: return ""
        return res

