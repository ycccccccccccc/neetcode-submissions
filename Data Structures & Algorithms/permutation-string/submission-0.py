class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        c = Counter(s1)

        for i, char in enumerate(s2):
            c[s2[i]] = c.get(s2[i], 0) - 1
            if c[s2[i]] == 0:
                del c[s2[i]]
            if i >= len(s1):
                c[s2[i-len(s1)]] += 1
                if c[s2[i-len(s1)]] == 0:
                    del c[s2[i-len(s1)]]
            if len(c) == 0:
                return True
    
        return False