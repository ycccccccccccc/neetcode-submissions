class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        def explore_island(index, x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return
            if grid[x][y] != "1":
                return
            grid[x][y] = index
            explore_island(index, x+1, y)
            explore_island(index, x, y+1)
            explore_island(index, x-1, y)
            explore_island(index, x, y-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "1":
                    continue
                islands += 1
                explore_island(islands, i, j)

        return islands
                