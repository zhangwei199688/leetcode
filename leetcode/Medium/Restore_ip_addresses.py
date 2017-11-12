'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''


class Solution(object):
    def restoreIpAddresses(self, s):
        re = []

        def restore(n, s, addr):
            if len(s) > 3 * n:
                return ''

            if n == 0:
                re.append(addr[:-1])
            else:
                for i in range(min(3, len(s))):
                    if (int(s[:i + 1]) <= 255) and (i == 0 or s[0] != '0'):
                        restore(n - 1, s[i + 1:], addr + s[:i + 1] + '.')

        restore(4, s, '')
        return re