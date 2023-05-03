class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        #print(nums1,nums2)
        a=[]
        for i in nums1:
            if i not in nums2:
                a.append(i)
            else:
                nums2.remove(i)
        print(a,nums2)
        return [a,nums2]