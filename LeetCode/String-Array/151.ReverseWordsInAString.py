'''
151. Reverse Words in a String

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
'''

####################################################################
Mine
####################################################################
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return( ' '.join( s.split()[::-1] ) )
        
####################################################################
Other_1
####################################################################
#@@ 思路是每一个部分先进行调转，整体再调转
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = s.split()
        for i, t in enumerate(ss):
            ss[i] = t[::-1]
        
        ss = ' '.join(ss)
        ss = ss[::-1]
        return ''.join(ss)


####################################################################
Other_1
####################################################################
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverse(ss, b ,d):
            c = None
            while b < d :
                c = ss[b]
                ss[b] = ss[d]
                ss[d] = c
                b += 1
                d -= 1

        s = list(s)
        if len(s)==0 or len(s)==1:
            return ''.join(s)
            
        i,j = 0,1
        while j < len(s)-1:
            if s[j]==' ' and s[j+1]!=' ':
                    i = j+1
                    j += 1
                    continue
            if s[j]!=' ' and s[j+1]==' ':
                    reverse(s, i, j)
            j += 1
        reverse(s, i, len(s)-1)
        reverse(s, 0, len(s)-1)
        return ''.join(s)
