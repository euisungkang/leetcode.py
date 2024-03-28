import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        maxScore, prefixSum, minHeap = float('-inf'), 0, []

        for a, b in sorted(list(zip(nums1, nums2)), key=itemgetter(1), reverse=True):
            prefixSum += a
            heappush(minHeap, a)
            if len(minHeap) == k:
                maxScore = max(maxScore, prefixSum * b)
                prefixSum -= heappop(minHeap)

        return maxScore