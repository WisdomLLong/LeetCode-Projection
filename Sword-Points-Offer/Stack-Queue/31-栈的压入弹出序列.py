'''
P168
问题：压栈顺序[1,2,3,4,5]，[4,5,3,2,1]是该压栈序列对应的一个弹出序列，但[4,3,5,1,2]就不是
注意：
1、判为FALSE的条件就是：所有数字都压入栈，但仍然没有找到下一个弹出的数字
'''

class solution(object):
    def ispoplist(self, pushlist, poplist):
        ans = []
        if len(pushlist) != len(poplist):
            return
        ans.append(pushlist.pop(0))
        while len(poplist) > 0:
            if len(pushlist) == 0 and ans[-1] != poplist[0]:
                return False
            if ans[-1] == poplist[0]:
                ans.pop()
                poplist.pop(0)
            else:
                ans.append(pushlist.pop(0))
        return True
        
print(solution().ispoplist([1,2,3,4,5], [4,5,3,1,2]))
