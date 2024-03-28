from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        queue = deque()
        for c in s:
            while (c in queue):
                queue.popleft()
            queue.append(c)
            longest = max(longest, len(queue))

        return longest