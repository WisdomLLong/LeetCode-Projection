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


##########################################################################
# Better Solution
##########################################################################
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    num1:=len(nums1)
    num2:=len(nums2)
    if num1==0&&num2==1{
        return float64(nums2[0])
    }else if num1==1&&num2==0{
        return float64(nums1[0])
    }
    
    array:=make([]int,num1+num2)
    local:=0
    var i int
    var j int
    i = 0
    j = 0
    for i<num1&&j<num2{
        if nums1[i]<=nums2[j]{
            array[local]=nums1[i]
            i++
            local++
        }else{
            array[local]=nums2[j]
            j++
            local++
        }
    }
    if i>=num1{
        for j<num2{
            array[local]=nums2[j]
            j++
            local++
        }
    }else if j>=num2{
        for i<num1{
            array[local]=nums1[i]
            i++
            local++
        }
    }
    //dan
    if local%2!=0{
        return float64(array[local/2]*1.0)
    }else{
        return float64((float64(array[local/2])+float64(array[local/2-1]))/2.0)
    }
}
