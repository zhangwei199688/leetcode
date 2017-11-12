'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        if root == None:
            return 0

        ldepth = self.minDepth(root.left)
        rdepth = self.minDepth(root.right)

        if ldepth == rdepth == 0:
            return 1
        if ldepth == 0 and rdepth != 0:
            return rdepth + 1
        if ldepth != 0 and rdepth == 0:
            return ldepth + 1
        else:
            return min(ldepth, rdepth) + 1