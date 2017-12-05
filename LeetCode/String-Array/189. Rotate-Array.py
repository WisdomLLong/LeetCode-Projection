'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
'''

##########################################################
# My Solution
##########################################################
'''
注意：list尾部元素尽量不要用 -1 来标识，容易出错
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        
        if  len(nums)==0 or k == 0:
            return
        
        def reverse(s, b, d):
            while b < d:
                c = s[b]
                s[b] = s[d]
                s[d] = c
                b += 1
                d -= 1
        
        reverse(nums, 0, len(nums)-k-1)
        reverse(nums, len(nums)-k, len(nums)-1)
        reverse(nums, 0, len(nums)-1)
        
        
                
