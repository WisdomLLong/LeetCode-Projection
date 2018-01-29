#############################################################
# Lazy Solution
# 对数组进行排序，取中间的那个数字
#############################################################
class Solution(object):
    def majorityElement(self, num):
    return sorted(num)[len(num)/2]
