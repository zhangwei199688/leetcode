'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''

class Solution(object):
    def climbStairs(self, n):
        a=0
        b=1
        for i in range(n):
            c=a+b
            a=b
            b=c
        return c

# A Fibonacci sequence,very simple one