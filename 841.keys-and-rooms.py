#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0]   # We start at room 0, thus add

        # DFS recursive to visit and record all unvisited rooms
        def DFSRecursive(curr) :

            if curr == [] :
                return []
            
            for r in curr :
                if r not in visited :
                    visited.append(r)
                    DFSRecursive(rooms[r])
                
        # Start with room 0
        DFSRecursive(rooms[0])
        
        return len(visited) == len(rooms)

        
    
    # Implementation with explicit definition of graphs as a
    # map of sets. Better to understand what happens with graphs,
    # but inefficient for the question

    # def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

    #     # Create a graph representation of all room connections
    #     graph = defaultdict(set)
    #     for i, k in enumerate(rooms) :
    #         graph[i] = k

    #     visited = [0]   # Use to track visited rooms

    #     # Recursive DFS to visit all non-visited rooms and record it 
    #     def DFSRecursive(curr) :
    #         if curr == [] :
    #             return []
            
    #         for r in curr :
    #             if r not in visited :
    #                 visited.append(r)
    #                 DFSRecursive(graph[r])
        
    #     # Room 0 is always open, thus we start there
    #     DFSRecursive(graph[0])

    #     return len(visited) == len(graph)

# @lc code=end

