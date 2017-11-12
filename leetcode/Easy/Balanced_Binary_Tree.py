'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        def t(n):
            if n==None:
                return 0
            ldeep=t(n.left)
            rdeep=t(n.right)
            return max(ldeep,rdeep)+1
        if not root:
            return True
        tree=[]
        tree.append(root)
        while tree:
            current=tree.pop(0)
            if abs(t(current.left)-t(current.right))>1 :
                return False
            if current.left != None:
                tree.append(current.left)
            if current.right != None:
                tree.append(current.right)
        return True

    #an iterative solution,to which I need to study
    class Solution(object):
        def isBalanced(self, root):

            def check(root):
                if root is None:
                    return 0
                left = check(root.left)
                right = check(root.right)
                if left == -1 or right == -1 or abs(left - right) > 1:
                    return -1
                return 1 + max(left, right)

            return check(root) != -1