class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        memo = nums[:k]
        heapq.heapify(memo)

        for num in nums[k:]:
            if num > memo[0]:
                heapq.heappop(memo)
                heapq.heappush(memo, num)


        return memo[0]  