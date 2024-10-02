class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # bb = sorted(set(arr))
        # d={}
        # c=1
        # for i in bb:
        #     d[i] = c
        #     c+=1
        # output = []
        # for i in arr:
        #     output.append(d[i])
        # return output
        arr2 = (sorted(set(arr)))
        rank_dict = {value: idx + 1 for idx, value in enumerate(arr2)}
        l=[rank_dict[num] for num in arr]
        return l