class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = sum(x for x in nums if x % 2 == 0)
        ans = []
        for val, idx in queries:
            # if original nums[idx] is even, then we deduct it from evenSum
            if nums[idx] % 2 == 0: evenSum -= nums[idx]
            # in-place update nums
            nums[idx] += val
            # check if we need to update evenSum for the new value
            if nums[idx] % 2 == 0: evenSum += nums[idx]
            # then we have evenSum after this query, push it to ans 
            ans.append(evenSum)
        return ans
