'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        if root == None:
            return []
        tree = []
        tree.append(root)
        lis = []
        d = []
        currentlevelnum = 1
        nextlevelnum = 0
        while tree:
            current = tree.pop(0)
            d.append(current.val)
            currentlevelnum -= 1
            if current.left != None:
                tree.append(current.left)
                nextlevelnum += 1
            if current.right != None:
                tree.append(current.right)
                nextlevelnum += 1
            if currentlevelnum == 0:
                currentlevelnum = nextlevelnum
                nextlevelnum = 0
                lis.append(d)
                d = []
        lis.reverse()
        return lis
