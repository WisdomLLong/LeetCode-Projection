'''
二维数字数组matrix中，每一行都从左到右递增排序，每一列都从上到下递增排序
问题：快速查找某个传入数字的位置
'''

'''
例子：
1   2   8   9
2   4   9   12
4   7   10  13
6   8   11  15
找到数字 7 的位置

从右上角排查，删除列
1   2   8 
2   4   9  
4   7   10 
6   8   11

1   2 
2   4  
4   7  
6   8  

删除行
2   4  
4   7  
6   8  

4   7  
6   8  
'''
