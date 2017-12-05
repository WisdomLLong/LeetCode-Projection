'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
'''

#########################################################################
# My Soultion
#########################################################################
'''
运行错误：最短路径长度错误
原因1：找不到标识深度的方法  # 自己是一枝一枝看的，别人是一行一行看的（或者一个集合一个集合看的）
原因2：尝试使树不回溯到已经查询过的节点上 # 暂时没有看到解决办法
'''
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        # 看两个词是否符合转换规则
        def to_transform(tran_1, tran_2):
            num = 0
            for i, t in zip(tran_1, tran_2):
                if i != t:
                    num += 1
            if num==1:
                return True
            else:
                return False
        
        # 找到临节点
        def if_in(tran_1):
            may_list = []
            for tran_2 in wordList:
                if to_transform(tran_1, tran_2):
                    may_list.append(tran_2)
            return may_list
        
        # 尝试判断搜索树的深度
        times = 0
        queue = [beginWord]
        begin_save = beginWord
        hang_1 = 1
        hang_2 = 0
        father = {}
        
        if endWord not in wordList:
            return 0            
        
        while queue:
            if queue[0]==begin_save:
                times += 1                
            find = queue.pop(0)
            hang_1 -= 1    
            if to_transform(find, endWord):
                times += 1
                break
            may_list = if_in(find)
                     
            # 删除返回到父节点的路径
            for i, t in enumerate(may_list):
                for ttt in father:
                    if father[ttt] == t:
                        may_list[i] = 0
            may_list = [i for i in may_list if i != 0]
            
            if len(may_list) == 0:
                continue
            
            for may in may_list:
                father[may] = find

            hang_2 = len(may_list) + hang_2
            if hang_1 == 0:
                hang_1 = hang_2
                hang_2 = 0
                begin_save = may_list[0]
            
            queue.extend(may_list)
        
        return times
        
#########################################################################
# Better Solution 1
#########################################################################
import string
from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        
        def getNbrs(src, dest, wordList):
            res = []
            for c in string.ascii_lowercase:
                for i in range(0, len(src)):
                    newWord = src[:i] + c + src[i+1:]
                    if newWord == src:
                        continue
                    if newWord in wordList or newWord == dest:
                        yield newWord
                        
        wordList = set(wordList)
        
        if endWord not in wordList:
            return 0
        
        queue = deque([beginWord])
        length = 0
        while queue:
            length += 1
            for k in range(0, len(queue)):
                top = queue.popleft()
                for nbr in getNbrs(top, endWord, wordList):
                    wordList.remove(nbr)
                    if nbr == endWord:
                        return length + 1
                    queue.append(nbr)
        return 0

#########################################################################
# Better Solution 2
#########################################################################

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordDict = set(wordList)
        length = 2
        front, back = set([beginWord]), set([endWord])
        wordDict.discard(beginWord)
        while front:
            # generate all valid transformations
            front = wordDict & (set(word[:index] + ch + word[index+1:] for word in front 
                                for index in range(len(beginWord)) for ch in 'abcdefghijklmnopqrstuvwxyz'))
            if front & back:
                # there are common elements in front and back, done
                return length
            length += 1
            
            if len(front) > len(back):  # 尽可能保证从上到下 和 从下到上的搜索树的个数相同！！！双向搜索！！！
                # swap front and back for better performance (fewer choices in generating nextSet)
                front, back = back, front   # 等号右边计算完同时赋值给左边
            # remove transformations from wordDict to avoid cycle
            wordDict -= front
        return 0    # 考虑小部分的情况，其他部分归为return 0，方便了操作
