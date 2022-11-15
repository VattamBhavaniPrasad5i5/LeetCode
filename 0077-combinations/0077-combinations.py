class Solution:
    def combine(self, n, k):
        sol=[]
        def backtrack(remain,comb,nex):
			# solution found
            if remain==0:
                sol.append(comb.copy())
            else:
				# iterate through all possible candidates
                for i in range(nex,n+1):
					# add candidate
                    comb.append(i)
					#backtrack
                    backtrack(remain-1,comb,i+1)
					# remove candidate
                    comb.pop()
            
        backtrack(k,[],1)
        return sol