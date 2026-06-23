class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(x**2+y**2, x, y) for x, y in points]
        distances.sort()
        return [[distances[i][1], distances[i][2]] for i in range(k)]