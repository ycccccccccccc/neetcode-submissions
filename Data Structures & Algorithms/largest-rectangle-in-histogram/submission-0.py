class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        positions = []
        l = len(heights)
        maxArea = 0

        for i in range(l+1):
            print(positions)
            while positions and (i == l or heights[positions[-1]] >= heights[i]):
                h = heights[positions.pop()]
                w = i if not positions else (i-positions[-1]-1)
                maxArea = max(maxArea, h*w)
            positions.append(i)

        return maxArea