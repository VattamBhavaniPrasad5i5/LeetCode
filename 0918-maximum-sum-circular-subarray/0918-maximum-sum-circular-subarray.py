class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        minHeap = [(0, -1)]  # (preSum, index)
        preSumSoFar = 0
        ans = nums[0]
        for i in range(2*n):
            preSumSoFar += nums[i % n]
            while minHeap and i - minHeap[0][1] > n:  # Remove if the index of minHeap.top() is out of range size `n`
                heappop(minHeap)
            preSumPrevious = minHeap[0][0]
            ans = max(ans, preSumSoFar - preSumPrevious)
            heappush(minHeap, (preSumSoFar, i))
        return ans