class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)

        while len(stones) > 1:
            print(stones)
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            print(s1, s2)
            if s1 < s2:
                heapq.heappush(stones, s1-s2)
        print(stones)
        return -stones[0] if len(stones) != 0 else 0