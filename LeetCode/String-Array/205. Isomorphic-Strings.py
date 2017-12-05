'''
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.
For example,
Given "egg", "add", return true.
Given "foo", "bar", return false.
Given "paper", "title", return true.
'''

'''
1、注意题意是说，s向t映射不能有一个字符映射向两个字符的情况，t向s映射同样不行
也就是： 
'aa' 'ab' ; 'ab' 'aa' 是False
'ab' 'ca' 却是True

2、zip的用法

3、试着举一些特殊的例子
'''

########################################################################
# My Soultion
########################################################################
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s)==0 or len(s)==1:
            return True
        
        # 如何判断是否为字母

        def discuss(key, value):
            dic = {}
            dic[key[0]] = value[0]
            i = 1
            while i < len(key):
                if key[i] in dic:
                    if value[i] != dic.get(key[i]):
                        return False            # 注意这里的return只会跳出一层函数
                    else:
                        i += 1
                        continue                # 这里完全没有必要用continue，因为不会再执行下面的else了
                else: 
                    dic[key[i]] = value[i]
                    i += 1
        
        key,value = s,t        
        if discuss(key, value)==False:
            return False
        key,value = t,s
        if discuss(key, value)==False:
            return False
                
        return True

########################################################################
# Better Soultion
######################################################################## 
# s = 'a a b a'
# t = 'c b c c'
#@@ 一列一列来看，除了相同列，每行不能再有相同的字符了
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))    

########################################################################
# Better Soultion
########################################################################
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        chars1 = {}
        chars2 = {}
        count = 1
        for c1, c2 in zip(s, t):
            if c1 in chars1 and c2 in chars2:
                if chars1[c1] != chars2[c2]:
                    return False
            elif c1 in chars1 or c2 in chars2:
                return False
            else:
                chars1[c1] = count
                chars2[c2] = count
                count += 1
                
        return True
