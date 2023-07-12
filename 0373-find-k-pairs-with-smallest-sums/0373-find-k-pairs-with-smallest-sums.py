class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1=len(nums1)
        n2=len(nums2)
        lst=[]
        heapq.heapify(lst)
        for i in range(n1):
            for j in range(n2):
                if k>0:
                    heapq.heappush(lst,(-1*(nums1[i]+nums2[j]),nums1[i],nums2[j]))
                    k-=1
                else:
                    pd,x,y=heapq.heappop(lst)
                    if nums1[i]+nums2[j]>=-1*pd:
                        heapq.heappush(lst,(pd,x,y))
                        break
                    else:
                        heapq.heappush(lst,(-1*(nums1[i]+nums2[j]),nums1[i],nums2[j]))
        flst=[]
        for i in range(len(lst)):
            pd,x,y=heapq.heappop(lst)
            flst.append((x,y))
        return flst