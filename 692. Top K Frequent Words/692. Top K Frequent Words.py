class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        dict = {}
        for x in words:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        print([i for i in sorted(dict.values())])
        res = sorted(dict, key=lambda x: (-dict[x], x))
        return res[:k]
