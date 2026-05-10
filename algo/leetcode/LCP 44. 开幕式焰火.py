# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def numColor(self, root: TreeNode) -> int:
        s = set()

        def f(r):
            nonlocal s
            if r == None:
                return

            s.add(r.val)
            f(r.left)
            f(r.right)

        f(root)

        return len(s)



