'''
1、如果使用位操作符号，十进制数是直接进行位操作的，显示仍然是十进制
2、某个十进制数的负数，等于二进制数的补码，即取反再加1
3、下面的操作相当于一步一步减去尾部的二进制1
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n>0:
            #n -= (n & -n)  # 利用补码进行操作
            n = (n-1)&n   # 利用减一进行操作，效果一样
            count += 1
        return count
