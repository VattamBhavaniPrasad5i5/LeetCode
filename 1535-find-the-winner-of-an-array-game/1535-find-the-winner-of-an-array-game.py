class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        c=0
        cur=arr[0]
        for i in range(1,len(arr)):
            if cur<arr[i]:
                cur=arr[i]
                c=0
            c+=1
            if c==k:
                break
        return cur