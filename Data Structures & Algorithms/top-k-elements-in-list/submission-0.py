class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        sorted_c = sorted([(times, num) for num, times in c.items()], reverse=True)
        return [sorted_c[i][1] for i in range(k)]