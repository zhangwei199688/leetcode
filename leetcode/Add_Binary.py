'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''
class Solution(object):
    def addBinary(self, a, b):
        sum=int(a)+int(b)
        for i in range(1,len(str(sum))+1):
            if int(str(sum)[-i])>=2:
                sum-=2*(10**(i-1))
                sum+=10**i
        return str(sum)

#It's a short but slow one...