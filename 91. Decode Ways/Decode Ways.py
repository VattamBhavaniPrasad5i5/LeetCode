class Solution:
	memo={}
	def numDecodings(self, s: str) -> int:        
		if len(s)==0:
			return 1
		if s[0]=="0":
			return 0
		if s[0]!="0" and len(s)==1:
			return 1

		outOfRange=0 if int(s[:2])>26 else 1
		output=0
		if s in self.memo.keys():
			return self.memo[s]
		else:
			output=self.numDecodings(s[1:])+outOfRange*self.numDecodings(s[2:])

		if s not in self.memo.keys():
			self.memo[s]=output

		return output
