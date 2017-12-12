'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
'''

'''
##########################################################################
# Better Solution 1
##########################################################################
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: float
        """
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
            
        imin, imax, half_len = 0, m, int((m + n + 1) / 2)
        while imin <= imax:
            i = int((imin + imax) / 2)  
            # while的停止条件，这里i的计算以及下面imin和imax的计算说明，0<=i<=m
            # i一直在以二分法的方式寻找中间值
            j = half_len - i
            # j只需要根据上面这个固定公式计算就可以了
            # i和j分别表示A和B的位于合并后序列的中间数位置
            if j > 0 and i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif j < n and i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                '''
                最终只可能出现三种情况：
                1、中间值位于A中间，B中间，此时A和B相当于交叉：B[j-1]<=A[i], A[i-1]<=B[j]
                2、A按照大小排序完全位于B的左边，此时i==m
                3、A按照大小排序完全位于B的右边，此时i==0
                '''
                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]   # 此时m==n
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]    # # 此时m==n
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

##########################################################################
# Better Solution 2
##########################################################################

class Solution:

    def getKth(self, A, B, k):
        lenA = len(A); lenB = len(B)
        if lenA > lenB: return self.getKth(B, A, k)
        if lenA == 0: return B[k - 1]
        if k == 1: return min(A[0], B[0])
        pa = min(int(k/2), lenA); pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)

    def findMedianSortedArrays(self, nums1, nums2):
        A,B = nums1,nums2
        lenA = len(A); lenB = len(B)
        if (lenA + lenB) % 2 == 1: 
            return self.getKth(A, B, (lenA + lenB)//2 + 1)
        else:
            return (self.getKth(A, B, (lenA + lenB)//2) + self.getKth(A, B, (lenA + lenB)//2 + 1)) * 0.5
        
            
