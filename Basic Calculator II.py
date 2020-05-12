class Solution(object):
    def infixToPostfix(self, infixexpr):
        prec = {}

        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1
        opStack = []
        postfixList = []
        temp = ""
        infixexpr = infixexpr.replace(' ','')
        tokenList = list(infixexpr)

        for token in tokenList:
            if token.isdigit():
                temp += token

            elif token == '(':
                opStack.append(token)
            elif token == ')':
                topToken = opStack.pop()
                postfixList.append(temp)
                temp = ""
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                postfixList.append(temp)
                temp = ""
                while (len(opStack) != 0) and (prec[opStack[-1]] >= prec[token]):
                      postfixList.append(opStack.pop())
                opStack.append(token)

        postfixList.append(temp)
        while len(opStack) != 0:
            postfixList.append(opStack.pop())
        return " ".join(postfixList)

    def postfixEval(self, postfixExpr):
        operandStack = []
        tokenList = postfixExpr.split()

        for token in tokenList:
            if token.isdigit():
                operandStack.append(int(token))
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = Solution.doMath(self, token, operand1, operand2)
                operandStack.append(result)
        if len(operandStack) > 1:
            operandStack = [str(item) for item in operandStack]
            res = ''.join(operandStack)
            return res
        return str(operandStack.pop())

    def doMath(self,op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 // op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2
    def calculate(self, s):

        s = Solution.infixToPostfix(self, s)
        result = Solution.postfixEval(self, s)
        return int(result)

print(Solution.calculate(0,"3+2*2"))
print(Solution.calculate(0," 3/2 "))
print(Solution.calculate(0," 3+5 / 2 "))

