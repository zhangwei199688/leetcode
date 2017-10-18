'''
Description:

Count the number of prime numbers less than a non-negative number, n.
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        flags = [1] * n  # Position 1..n-1 are flags of prime numbers for 1..n-1
        flags[0] = flags[1] = 0  # 0, 1 are not prime

        for i in range(2, int(n ** 0.5) + 1):
            if flags[i] == 1:  # Fill flags for position i*i, i*(i+1), ..., n
                flags[i * i:n:i] = [0] * len(flags[i * i:n:i]) # 用步长代替乘法

        return sum(flags)