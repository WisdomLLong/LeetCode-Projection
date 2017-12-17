'''
斐波那契数列
f(n) = 
0   if n==0
1   if n==1
f(n-1)+f(n-2)     n>1
'''

'''
递归固然简单书写，但因为会计算重复的节点，使得时间复杂度以n的指数的方式递增
而下面的做法是自下而上的做法，复杂度为O(n)
'''
class Fibonacci(object):
    def produce(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            f1 = 1
            f0 = 0
            i = 2
            while i <= n :
                data = f0 + f1
                f0 = f1
                f1 = data
                i += 1
            return data
                
        
a = Fibonacci().produce(6)
print(a)
