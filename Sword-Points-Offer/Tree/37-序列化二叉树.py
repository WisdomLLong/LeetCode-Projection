'''
注意：
1、这里的递归用的极其精妙！
'''

class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def Serialize(self, root):
        if root != None:
            return [root.val] + self.Serialize(root.left) + self.Serialize(root.right)
        else:
            return ['#']

    def Deserialize(self, s):
        self.s = s      #@@ 转换为全局变量有助于递归函数的调用
        return self.rDLF()
        
    def rDLF(self):
        temp = self.s.pop(0)
        if temp != '#':
            root = TreeNode(temp)
            root.left = self.rDLF()
            root.right = self.rDLF()
        else:
            root = None
        return root
