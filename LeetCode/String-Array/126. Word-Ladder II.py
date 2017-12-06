'''
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
'''

'''
1、变量名 = collections.defaultdict(数据类型)
产生一个特殊的dict，其key正常，但value可以是Iterable类型的数据，不再只能存一个值

2、目的在于存储子节点与父节点之间的对应关系，并且不再只有一径
'''

###########################################################################
Better Solution_1
###########################################################################
from collections import deque
class Solution:
    def findLadders(self, start, end, dic):
        dic = set(dic)
        if end not in dic:
            return []
        
        dic.add(end)
        level = set([start])
        # key is word, value is parent word, e.g. {'hot': set(['hit']), 'cog': set(['log', 'dog'])}
        # In each level, defaultdict(set) can remove duplicates, first we need to get parent dictionary
        parents = collections.defaultdict(set)
        while level and end not in parents:
            next_level = collections.defaultdict(set)
            for word in level:
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(start)):
                        childWord = word[:i] + char + word[i+1:]
                        if childWord in dic and childWord not in parents: next_level[childWord].add(word)
            level = next_level
            parents.update(next_level)
             
        # then according parent dictionary, build result from end word to start word
        res = [[end]]
        while res and res[0][0] != start:
            res = [[p] + r for r in res for p in parents[r[0]]]
        return res

