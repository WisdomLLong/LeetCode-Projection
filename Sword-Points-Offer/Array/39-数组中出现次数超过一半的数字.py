'''
P205
'''


#############################################################
# Lazy Solution
# 对数组进行排序，取中间的那个数字
#############################################################
class Solution(object):
    def majorityElement(self, num):
    return sorted(num)[len(num)/2]


#############################################################
# Better Solution
#############################################################
'''
遍历整个数组的每一个元素，并存储两个数据，一个是元素的值，一个是它的'次数'，如果次数变为零，则用最新的元素数据来代替
总之，出现次数超过一半的元素必然可以留到最后
'''
class Solution(object):
    def majorityElement(self, num):
        
        if num == None:
            return False
        
        save_data = num[0]
        save_number = 1
        for data in num[1:]:
            if data == save_data:
                save_number += 1
            else:
                save_number -= 1
                if save_number == 0:
                    save_data = data
                    save_number = 1
                    
        return save_data
        
print(Solution().majorityElement([2,4,3,1,2,2,2]))
