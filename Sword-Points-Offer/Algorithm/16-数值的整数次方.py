'''
P113
1、考虑底数是0，指数是一个小于等于0的情况
2、Python 负数二进制 右移一位 最多只到-1
3、斐波那契数列解法，利用递归
'''

class Solution:
    def exp(self, base, exponent):
        InvalidInput = False
        if base == 0 and exponent<=0:
            InvalidInput = True
            return 0
        if exponent == 0:
            return 1
        if exponent < 0:
            unsigned_exponent = -exponent
        result = self.exponentdata(base, unsigned_exponent)
        if exponent < 0:
            return 1.0/result
        return [result, InvalidInput]
        
    def exponentdata(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        
        result = self.exponentdata(base, exponent>>1)
        result *= result
        if exponent & 1 == 1:
            result *= base
        
        return result
        

        
print(Solution().exp(2.0, 0))
