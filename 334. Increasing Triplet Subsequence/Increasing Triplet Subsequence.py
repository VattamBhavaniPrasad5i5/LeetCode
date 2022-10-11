  i=j=float('inf')
        for k in nums:
            if i>=k:
                i=k
            elif j>=k:
                j=k
            else:
                return True
        return False
