class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.output =[]
        return self.partitionHelper(s,{})
        
    def partitionHelper(self,available,dp):
        # Base Cases
        if len(available) ==1:
            return [[available]]
        if not available:
            return [[]]
        if available in dp:
            return dp[available]
        
        # Choice Tree
        res =[]
        for i in range(1,len(available)+1):
            first = available[:i] # first substring
            second = available[i:] # second substring
            if first == first[::-1]: # if first substring is a palindrome , then call the recursive function on second
                # Get the ans from below and prepend [first] to it
                result = self.partitionHelper(second,dp)
                temp =[]
                # result can be array of array i.e multiple possibilites for a subproblem
                # e.g. if recursive call is for subproblem "aab" , then ans can be ['aa,b'] and ['a','a',b]
                # so result will be [['aa,b'], ['a','a',b]]
                # prepend "first" substring to all possible solution we got from second substring recursive call and then put it in "res" variable and pass it above in the function call
                for r in result:
                    temp.append([first]+r)
                # don't do res.append(temp)
                res += temp
        dp[available] =res
        return dp[available]