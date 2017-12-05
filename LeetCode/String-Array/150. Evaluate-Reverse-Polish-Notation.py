'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''

'''
1、append和pop的使用
'''

#######################################################################
# My Solution
#######################################################################
#@@ Time Limit Exceeded！！！
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        tokens_save = tokens
        while len(tokens_save) != 1:
            for i, t in enumerate(tokens_save):
                if t=='*' or t=='/' or t=='+' or t=='-':
                    g={
                        '*': lambda : str(int(float(tokens_save[i-2])*float(tokens_save[i-1]))),
                        '/': lambda : str(int(float(tokens_save[i-2])/float(tokens_save[i-1]))),
                        '+': lambda : str(int(float(tokens_save[i-2])+float(tokens_save[i-1]))),
                        '-': lambda : str(int(float(tokens_save[i-2])-float(tokens_save[i-1]))),
                    }.get(t)
                    tokens_save[i] = g()
                    tokens_save.pop(i-2)
                    tokens_save.pop(i-2)
                    break
        return int(float(tokens_save[0]))
        
#######################################################################
# Better Solution
#######################################################################
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b, a = stack.pop(), stack.pop()
                if token == "+":
                    res = a + b
                if token == "-":
                    res = a - b
                if token == "*":
                    res = a * b
                if token == "/":
                    res = int(float(a) / float(b))
                stack.append(res)
            else:
                stack.append(int(token))
        return stack.pop()


