'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''
class Solution(object):
    def titleToNumber(self, s):
        num,i=0,0
        for item in s[::-1]:
            num+=(26**i)*(ord(item)-64)
            i+=1
        return num