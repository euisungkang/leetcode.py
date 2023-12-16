#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites : return True

        graph = defaultdict(lambda:[])

        for a, b in prerequisites :
            graph[a].append(b)
        
        # All nodes we have to visit at least once
        visiting = set()
        def dfs(curr) :
            
            if curr in visiting :
                return False

            if not graph[curr] :
                return True
            
            visiting.add(curr)
            for p in graph[curr] :
                if not dfs(p) :
                    return False
            visiting.remove(curr)

            graph[curr] = []
            return True

        for start in range(numCourses) :
            if not dfs(start) :
                return False
            
        return True
    
# @lc code=end

