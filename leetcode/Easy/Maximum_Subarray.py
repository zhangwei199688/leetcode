'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

class Solution(object):
    def maxSubArray(self, nums):
        maxnum=nums[0]
       # if len(nums)==1:
       #     return maxnum
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                subarray=nums[i:j]
                s=0
                for item in subarray:
                    s+=item
                if s>maxnum:
                    maxnum=s
        return maxnum

My solution,the only probelme is way too complicated that exceed the time limit
'''

#Solution on the Internet

class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum