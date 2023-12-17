#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        maxEffort = 0
        rows, cols = len(heights), len(heights[0])

        heap = [(0, 0, 0)]  # (effort, i, j)
        visited = set()

        while heap :
            curr = heapq.heappop(heap)
            i, j = curr[1], curr[2]
            visited.add((i, j))
            maxEffort = max(maxEffort, curr[0])

            # Reached End 
            if i == rows - 1 and j == cols - 1 :
                return maxEffort

            # Down
            if i + 1 < rows and (i + 1, j) not in visited:
                heapq.heappush(heap, (abs(heights[i + 1][j] - heights[i][j]), i + 1, j))
            # Right
            if j + 1 < cols and (i, j + 1) not in visited:
                heapq.heappush(heap, (abs(heights[i][j + 1] - heights[i][j]), i, j + 1))
            # Up
            if i - 1 >= 0 and (i - 1, j) not in visited:
                heapq.heappush(heap, (abs(heights[i - 1][j] - heights[i][j]), i - 1, j))
            # Left
            if j - 1 >= 0 and (i, j - 1) not in visited:
                heapq.heappush(heap, (abs(heights[i][j - 1] - heights[i][j]), i, j - 1))

        return maxEffort

# @lc code=end

