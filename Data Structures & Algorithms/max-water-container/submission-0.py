class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        vol = min(heights[l], heights[r]) * r
        while l < r:
            if heights[l] < heights[r]:
                new_l = l + 1
                while heights[l] > heights[new_l]:
                    new_l += 1
                vol = max(vol, min(heights[new_l], heights[r]) * (r-new_l))
                l = new_l
            else:
                new_r = r - 1
                while heights[r] > heights[new_r]:
                    new_r -= 1
                vol = max(vol, min(heights[l], heights[new_r]) * (new_r-l))
                r = new_r
        return vol