class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        p0, p1, p2 = False, False, False
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                if not p0 and t[0] == target[0]:
                    p0 = True
                if not p1 and t[1] == target[1]:
                    p1 = True
                if not p2 and t[2] == target[2]:
                    p2 = True
            if p0 and p1 and p2:
                return True
        return False