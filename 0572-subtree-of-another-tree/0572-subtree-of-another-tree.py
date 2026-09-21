# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        if subRoot is None:
            return True
        
        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def isSameTree(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        if root1 is None and root2 is None:
            return True
        
        if (root1 is not None and root2 is not None):
            return (root1.val == root2.val) and (self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right))

        return False
            
        
        