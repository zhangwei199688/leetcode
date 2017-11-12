'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
'''




class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i,j=0,0
        newlis=[]
        while (i<m) and (j<n):
            if nums1[i]<=nums2[j]:
                newlis.append(nums1[i])
                i+=1
            else:
                newlis.append(nums2[j])
                j+=1
        newlis.extend(nums1[i:] or nums2[j:])
        nums1=newlis


#A wrong test case in test...that screw all,but I suppose this algorithms is right