# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        mx = float("-inf")
        def dfs(node, mx):
            if not node:
                return 0
            count = 0
            if node.val >= mx:
                mx = node.val
                count +=1
            left = dfs(node.left, mx)
            right = dfs(node.right, mx)
            return  count + left + right
        return dfs(root,mx)

        