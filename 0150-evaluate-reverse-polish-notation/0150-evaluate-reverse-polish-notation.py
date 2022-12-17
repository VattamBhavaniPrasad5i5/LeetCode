class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        oper=["+","-","*","/"]
        arr=[]
        if len(tokens)==1:
            return int(tokens[0])
        for i in tokens:
            if i in oper:
                if i=='+':
                    a=int(stack[-2])+int(stack[-1])
                elif i=='-':
                     a=int(stack[-2])-int(stack[-1])
                elif i=='*':
                     a=int(stack[-2])*int(stack[-1])
                else :
                     a=int(stack[-2])/int(stack[-1])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(a)
                
            else:
                stack.append(i)
        return int(stack[0])