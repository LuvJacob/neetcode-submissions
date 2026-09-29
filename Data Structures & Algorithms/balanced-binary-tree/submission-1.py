# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = [True]
        def maxDepth(root: Optional[TreeNode]):
            if not root:
                return 0
            left_depth = maxDepth(root.left)
            right_depth = maxDepth(root.right)
            temp = abs(left_depth-right_depth)
            if temp > 1:
                balance[0] = False
            return max(left_depth,right_depth) + 1
        maxDepth(root)
        return balance[0]
        
        