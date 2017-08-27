'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result ^= i
        return result

#XOR algorithm
#a^a=0
#a^(b^c)=(a^b)^c