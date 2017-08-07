'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.


'''


class Solution(object):
    def plusOne(self, digits):
        digits[-1] += 1
        for i in range(1, len(digits) + 1):
            if i != len(digits):
                if digits[-i] > 9:
                    digits[-i] = 0
                    digits[-i - 1] += 1
                else:
                    return digits
        if digits[0] > 9:
            digits[0] = 0
            digits.insert(0, 1)
        return digits


#Your runtime beats 95.00 % of python submissions.
