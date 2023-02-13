class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if low==high and low%2==1:
            return 1
        
        if low%2==0:
            res=high-low
            if res>1 and res%2==0:
                return res//2
            elif res==1:
                return 1
            else:
                return (res+1)//2
        else:
            res=high-low
            if res>1 and res%2==0:
                return (res//2)+1
            elif res==1:
                return 1
            else:
                return ((res+1)//2)