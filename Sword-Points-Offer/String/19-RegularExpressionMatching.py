'''
问题：正则表达式匹配

实际上可以简化为DP。
设dp[i][j]的值为s[0:i]与p[0:j]是否匹配，其中[0:i]表示下标为0到i-1的子串，则：
1.若p[j-1]为 “*”，此时有两种情况可以使s[0:i]和p[0:j]匹配：一是s[0:i]与p[0:j-2]相匹配（因为 “*” 可以匹配0个字符），二是s[0:i-1]与p[0:j]匹配且字符s[i-1]与p[j-2]匹配；
2.如果p[j-1]不为 “*”，此时只需看s[0:i-1]与p[0:j-1]是否匹配且字符s[i-1]与p[j-1]是否匹配。
'''

class Solution(object):  
    def isMatch(self, s, p):  
        """ 
        :type s: str 
        :type p: str 
        :rtype: bool 
        """  
        dp=[[False for col in range(len(p)+1)]for row in range(len(s)+1)]  
        dp[0][0]=True  
        for i in range(len(s)+1):  
            for j in range(1,len(p)+1):  
                if j>1 and p[j-1]=='*':  
                    dp[i][j]=dp[i][j-2] or (i>0 and (s[i-1]==p[j-2] or p[j-2]=='.')) and dp[i-1][j]  
                else:  
                    dp[i][j]=i>0 and dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='.')  
        return dp[len(s)][len(p)]  
