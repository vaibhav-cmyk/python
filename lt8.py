import numpy as np
nums1 = [1,3,4,5,6,7,8]
nums2 = [2,3,5,2,4]

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        result=np.concatenate((nums1,nums2))
        return result
    
res=Solution()
t=res.findMedianSortedArrays(nums1,nums2)
print(t)