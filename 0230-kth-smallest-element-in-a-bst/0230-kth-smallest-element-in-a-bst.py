# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        res = list()
        def inorder(root):
            if root is None:
                return
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

            return res
        
        return inorder(root)[k-1]
        
        