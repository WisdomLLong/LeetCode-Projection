'''
问题：
注意：
1、第一步：求所有可能出现在第一个位置的字符，即把第一个字符和后面所有的字符交换
2、第二步：固定第一个字符，求后面所有字符的排列
'''


def Permutation(string,i):  
    if string == None:  
        return  
    if string[i] == '\n':  
        print("%s\n"%string)  
    else:  
        for j in range(i,len(string)-1):              
            string[j],string[i] = string[i],string[j]  
            # 交换位置后，输出以list[j]不变，后面的字母改变的所有排列
            Permutation(string,i+1)  
            string[j],string[i] = string[i],string[j]  
            # 将转换后的字母恢复到原来的位置

# Test
string = ['a','b','c','d','\n']  
Permutation(string,0)    
