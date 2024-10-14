class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #initialize the heap by converting the existing numbers in nums into negative in order to find max in nums
        nums = [-num for num in nums] #the actual array with negative numbers
        heapq.heapify(nums) #converting to the heap
        score = 0 #our result
        while k > 0:
            a = -heapq.heappop(nums) #to get the maximum number in array
            score += a
            if a%3 == 0:
                b = a // 3
            else:
                b = (a // 3) + 1
            heapq.heappush(nums,-b) #adding the new number by dividin to the 3
            k -= 1 #decrement the k
        return score