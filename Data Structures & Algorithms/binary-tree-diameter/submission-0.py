# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = [0]
        def max_depth(root: Optional[TreeNode]):
            if not root:
                return 0
            left_depth = max_depth(root.left)
            right_depth = max_depth(root.right)
            temp = left_depth + right_depth
            if temp > diam[0]:
                diam[0] = temp
            return max(left_depth,right_depth)+1
        max_depth(root)
        return diam[0]
        