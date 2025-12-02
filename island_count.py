# https://leetcode.com/problems/number-of-islands/
# Source: https://www.youtube.com/watch?v=o8S2bO3pmO4
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        if not self.grid or len(self.grid) == 0:
            return 0
        island_count = 0
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                if self.grid[i][j] == "1":
                    island_count += self.dfs(i, j)
        return island_count
    
    def dfs(self, i, j):
        if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[i]) or self.grid[i][j] == "0":
            return 0
        else:
            self.grid[i][j] = "0"
            self.dfs(i-1, j)
            self.dfs(i+1, j)
            self.dfs(i, j-1)
            self.dfs(i, j+1)
            return 1