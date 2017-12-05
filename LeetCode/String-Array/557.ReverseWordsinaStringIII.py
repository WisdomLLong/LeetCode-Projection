'''
Given a string, you need to reverse the order of characters 
in each word within a sentence while still preserving whitespace and initial word order.

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''
####################################################################
# Mine
####################################################################

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_save = list(s)
        s_save.append(' ')
        s_reverse = []
        b,d = 0,0
        for i, j in enumerate(s_save):
            if j==' ':
                d = i
                s_data = s_save[b : d]
                s_reverse.append(''.join(s_data[::-1]))   
                b = d+1
        return(' '.join(s_reverse))
        
        
####################################################################
# Other_1
####################################################################
@@ 关键在于split的使用

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return( ' '.join([i[::-1] for i in s.split()]) )

