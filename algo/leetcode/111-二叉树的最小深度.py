# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.min_d = float('inf')

        def dfs(r, c = 1):
            if not r.left and not r.right:
                self.min_d = min(self.min_d, c)

            if r.left:
                dfs(r.left, c + 1)
            if r.right:
                dfs(r.right, c + 1)

        dfs(root)

        return self.min_d

