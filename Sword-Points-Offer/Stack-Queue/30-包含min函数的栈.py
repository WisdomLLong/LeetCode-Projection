'''
P165
问题：维护一个栈，使得min的时间复杂度为O(1)
注意：
1、用一个辅助栈存储最小值
'''

class stack(object):
    def __init__(self):
        self.main_stack = []
        self.assit_stack = []
    def new_push(self, value):
        self.main_stack.append(value)
        if value<self.assit_stack[-1] or self.assit_stack == []:
            self.assit_stack.append(value)
        else:
            self.assit_stack(self.assit_stack[-1])
    def new_pop(self):
        if self.assit_stack == []:
            return []
        self.assit_stack.pop
        return self.main_stack.pop
    def new_min(self):
        return self.assit_stack[-1]
