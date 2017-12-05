'''
List length is n ; Size of the number in list is 0~n-1
Input: [2, 3, 1, 0, 2, 5, 3]
Output: 2 or 3
'''

'''
1、看数字是否放在与这个数字相同的下标的位置上
2、如果不是：
比较是否相同，相同就找到了；
不相同：调换位置
'''

######################################################
# 空间复杂度为o(1) （通过改变位置查重）
######################################################
class Solution(object):
    def rotate(self, nums):
        
        if isinstance(nums, list)==False:
            return False
        
        def size(data):
            return data > len(nums)-1 or data <0
        if list(filter(size, nums))!=[] :
            return False
        
        
        if len(nums)==0 or len(nums)==1:
            return
            
        def reverse(s, b, d):
            c = s[b]
            s[b] = s[d]
            s[d] = c
        
        i = 0
        while i < len(nums):
            if nums[i]==i:
                i += 1
                continue
            else:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    reverse(nums, i, nums[i])

a = Solution()
print(a.rotate([2, 3, 1, 0, 2, 5, 3]))

######################################################
# 空间复杂度为o(1)，不改变数组内容 （二分法：通过范围内的个数查重）
######################################################
class Solution(object):
    def rotate(self, nums):
        
        data_max = len(nums)-1
        
        if isinstance(nums, list)==False:
            return False
        
        def size(data):
            return data > data_max or data <0
        if list(filter(size, nums))!=[] :
            return False
        
        if len(nums)==0 or len(nums)==1:
            return False
            
        def numbers(s, size_low, size_high):
            number = 0
            for i in s:
                if i >= size_low and i <= size_high:
                    number += 1
            return number
        
        start,end = 1,data_max
        while start<=end:
            middle = int((end-start)/2)+start
            sum_a = numbers(nums, start, middle)
            if start==end:
                if sum_a>1:
                    return start
                else:
                    break
            if sum_a > middle-start+1:
                end = middle
            else:
                start = middle+1
        return False

a = Solution()
print(a.rotate([2, 3, 5, 4, 3, 2, 6, 7]))


