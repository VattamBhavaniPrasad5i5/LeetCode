class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # frequency table to store the frequency of the remainder
        remainderFrq = defaultdict(int)
        # Empty sub array will have a sum of 0 and remainder of 0, thus the frequency of 0 is 1 before we go into the array
        remainderFrq[0] = 1
        
        res = prefixSum = 0
        for n in nums:
            # Adding n to the prefixSum, so we have the prefixSum up to the ith position.
            prefixSum += n
            # Get the remainder of the current prefixSum.
            remainder = prefixSum % k
            # We need to increase the result before update the frequency table.
            # Because we are counting how many previous prefixSum have the same remainder.
            res += remainderFrq[remainder]
            # Update the frequency table.
            remainderFrq[remainder] += 1
        return res