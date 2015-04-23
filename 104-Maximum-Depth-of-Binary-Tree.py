__author__ = 'xuweitao'
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        depth = 0

        if root != None:
            leftDepth = self.maxDepth( root.left )
            rightDepth= self.maxDepth( root.right )

            depth = leftDepth + 1 if ( leftDepth >= rightDepth ) else rightDepth + 1

        return depth