class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        if h == len(piles): return max_rate

        l, r = 1, max(piles)
        while l <= r:
            hours = 0
            m = (l+r)//2
            for p in piles:
                hours += math.ceil(p/m)
            if hours > h:
                l = m + 1
            else:
                r = m - 1

        return l



