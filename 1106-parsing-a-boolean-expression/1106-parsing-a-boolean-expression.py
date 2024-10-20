class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        expressions = []
        stack = []
        for i in expression:
            if i in ['&', '|', '!']:
                expressions.append(i)
            elif i == ')':
                x = stack.pop()
                if expressions[-1] == '&':
                    temp = True
                elif expressions[-1] == '|':
                    temp = False
                else:
                    stack.pop()
                    expressions.pop()
                    var = 'f' if x == 't' else 't'
                    stack.append(var)
                    continue
                while x != '(':
                    var = False if x == 'f' else True
                    if expressions[-1] == '&':
                        temp = temp and var
                    else:
                        temp = temp or var
                    x = stack.pop()
                var = 't' if temp == True else 'f'
                stack.append(var)
                expressions.pop()
            elif i != ',':
                stack.append(i)
            #print(stack, expressions)
        return True if stack[-1] == 't' else False