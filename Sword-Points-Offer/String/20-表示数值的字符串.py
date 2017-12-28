'''
P127
例如字符串"123.45e+6"就是一个表示数值的字符串
'''

###################################################
Lazy Solution 1
###################################################
class solution(object):
    def isNumber(self, string):
        try:
            float(string)
            return True
        except:
            return False
           
###################################################
Lazy Solution 2
###################################################         
class solution(object):
    def isNumber(self, string):
        return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$",string)
        
'''
[]    表示字符
r"  " 表示原生字符串，省略正则表达式中的反斜杠
^     匹配字符串开头，在多行模式中匹配每一行开头
?     匹配前一个字符0次或1次
*     匹配前一个字符0或无限次
()    表示分组
$     匹配字符串结尾，在多行模式中匹配每一行的末尾
'''

###################################################
Corny Solution
###################################################  
class Solution(object):
    def isNumeric(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def scanUnsignedInteger(s, index):
            before = index[0]
            while s[index[0]] in "123456789":
                index[0] += 1
                try:
                    s[index[0]]
                except:
                    return True
            return index[0] != before

            
        def scanInteger(s, index):
            if s[index[0]] in "+-":
                index[0] += 1
            return scanUnsignedInteger(s, index)
        
        index = [0]      
        # s = list(s)
        numeric = scanInteger(s, index)
        
        if s[index[0]] == '.':
            index[0] += 1
            numeric = scanUnsignedInteger(s, index) or numeric
        
        if s[index[0]]=='e' or s[index[0]]=='E':
            index[0] += 1
            numeric = numeric and scanInteger(s, index)
            
        return numeric and index[0] == len(s)
                
print(Solution().isNumeric("123.45e+6"))
