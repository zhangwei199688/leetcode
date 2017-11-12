'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
class Solution(object):
    def majorityElement(self, nums):
        from collections import Counter
        c=Counter(nums)
        setnum=set(nums)
        a=len(nums)
        for ele in setnum:
            if c[ele]> (a/2.0):
                return ele