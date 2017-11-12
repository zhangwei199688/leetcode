'''
Implement int sqrt(int x).

Compute and return the square root of x.

'''


class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        low,high=1,x
        while (low<=high):
            cent=(low+high)/2
            if cent**2==x:
                return cent
            elif cent**2>x:
                high=cent-1
            else:
                low=cent+1
        return high


# Binary Solution 二分法

#A solution from leetcode ,which is a 35ms solution that beat the most

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r * r > x:
            r = (r + x / r) / 2

        return r

    #I don't quite understand