class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        c = Counter(s)
        for dt in t:
            if dt not in c or c[dt] == 0:
                return False
            c[dt] -= 1
        return True