'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        def left(n):
            return n and (n.val, left(n.left), left(n.right))

        def right(n):
            return n and (n.val, right(n.right), right(n.left))

        if not root or root.left == root.right == None: return True
        if root.left and root.right and root.left.val == root.right.val:
            return left(root.left) == right(root.right)
        else:
            return False


#learn and applicate