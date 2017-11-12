'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.


'''
class Solution(object):
    def isPalindrome(self, s):
        import re
        lis=[]
        st=s.lower()
        for i in st:
            if  re.match('^[0-9a-z]+$',i):
                lis.append(i)
        str1="".join(lis)
        lis.reverse()
        str2="".join(lis)
        if str1==str2:
            return True
        return False

 class Solution(object):
        def isPalindrome(self, s):
            """
            :type s: str
            :rtype: bool
            """
            alphanumerics = [c for c in s.lower() if c.isalnum()]
            return alphanumerics == alphanumerics[::-1]

#Im a fool.....