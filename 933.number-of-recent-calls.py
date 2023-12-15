#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
class RecentCounter:

    #Use Queue of times
    def __init__(self):
        self.requests = deque()


    def ping(self, t: int) -> int:
        self.requests.append(t)

        # Remove all pings that have expired
        while self.requests[0] < t - 3000 :
            self.requests.popleft()

        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

