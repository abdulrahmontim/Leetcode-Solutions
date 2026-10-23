# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxPath = float("-inf")

        def pathSum(node):
            nonlocal maxPath
    
            if node is None: return 0

            left = pathSum(node.left)
            right = pathSum(node.right)

            maxPath = max(maxPath, node.val + max(0, left) + max(0, right))
            return node.val + max(0, max(left, right))
        
        pathSum(root)
        return maxPath
        