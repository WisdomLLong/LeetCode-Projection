'''
P129
在一个数字数组当中，调整位置，使得所有偶数位于奇数后面，关键是利用前后的两个指针
'''

class Solution(object):
    def changeStation(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0 or len(s)==1:
            return s
        
        index_before = 0
        index_after = len(s)-1

        while index_before < index_after:
            while s[index_before] % 2 != 0:
                index_before += 1
            while s[index_after] % 2 == 0:
                index_after -= 1
            if index_before < index_after:
                s[index_after], s[index_before] = s[index_before], s[index_after]
        return ''.join(s)
                
print(Solution().changeStation([1 5 6 4 3 7 8 9 6 4 2]))
