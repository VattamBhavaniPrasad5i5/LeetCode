class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        al=0
        bo=0
        for i in range(1,len(colors)-1):
            if (colors[i]=='A' and colors[i]==colors[i-1] and colors[i]==colors[i+1]):
                al+=1
            elif (colors[i]=='B' and colors[i]==colors[i-1] and colors[i]==colors[i+1]):
                bo+=1
        if(al>bo):
            return(True)
        else:
            return(False)