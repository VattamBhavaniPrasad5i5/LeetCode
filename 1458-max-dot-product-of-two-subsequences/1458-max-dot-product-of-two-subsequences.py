from sys import maxsize
class Solution:
    def __init__(self):
        self.cache = {}

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        return self.maxProduct(nums1, nums2, currentIndex1=0, currentIndex2=0)
    
    def maxProduct(self, nums1, nums2, currentIndex1, currentIndex2):
	    #  Base Condition
        if currentIndex1 >= len(nums1) or currentIndex2 >= len(nums2):
            return -maxsize
        
		# Caching / Memoization
        currentKey = (currentIndex1, currentIndex2)
        if currentKey in self.cache:
            return self.cache[currentKey]
        
		# Recursive Calls
        normal = self.maxProduct(nums1, nums2, currentIndex1 + 1, currentIndex2 + 1)
        one = self.maxProduct(nums1, nums2, currentIndex1 + 1, currentIndex2)
        two = self.maxProduct(nums1, nums2, currentIndex1, currentIndex2 + 1)
        
		# take the currentProduct
        currentProduct = nums1[currentIndex1] * nums2[currentIndex2]
        
        self.cache[currentKey] = max(
		   currentProduct, 
		   currentProduct + normal,
		   normal, one, two
        )
        
        return self.cache[currentKey]