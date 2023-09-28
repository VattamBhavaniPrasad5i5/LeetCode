class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd,ev=[],[]
        for i in nums:
            if i%2!=0:
                print(i)
                odd.append(i)
            else:
                ev.append(i)
        print(odd,nums)
        return ev+odd