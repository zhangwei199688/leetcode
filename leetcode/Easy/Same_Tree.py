# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        def t(n):
            return n and (n.val, t(n.left), t(n.right))

        return t(p) == t(q)

#new way I've learnt from the discussion,pretty brilliant