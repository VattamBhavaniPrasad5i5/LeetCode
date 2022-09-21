class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        cnt = 0 
        for x in data:
            x = bin(x)[2:].zfill(8)
            if cnt: # in the middle of multi-byte 
                if x.startswith("10"): cnt -= 1
                else: return False 
            else: # beginning 
                cnt = x.find("0")
                if cnt == -1 or cnt == 1 or cnt > 4: return False 
                if cnt: cnt -= 1
        return cnt == 0
