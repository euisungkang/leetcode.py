#
# @lc app=leetcode id=2497 lang=python3
#
# [2497] Maximum Star Sum of a Graph
#

# @lc code=start
from collections import defaultdict
import heapq

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(lambda : [])
        for a,b in edges :
            if vals[b] > 0 :
                graph[a].append(vals[b])
            if vals[a] > 0 :
                graph[b].append(vals[a])

        maxStarSum = max(vals)
        
        for i in range(len(vals)) :
            kLargest = heapq.nlargest(k, graph[i])
            currentMax = vals[i] + sum(kLargest)
            maxStarSum = max(maxStarSum, currentMax)

        return maxStarSum
    
# @lc code=end

