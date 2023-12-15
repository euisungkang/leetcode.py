#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

# @lc code=start
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [*range(1, 1001)]
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        return heapq.heappop(self.heap)
        
    def addBack(self, num: int) -> None:
        if (num not in self.heap) :
            heapq.heappush(self.heap, num)
        
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
            
# @lc code=end

