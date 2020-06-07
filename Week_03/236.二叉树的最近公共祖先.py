# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        def DFS(node, p, q):
            if not node or node in [p, q]:
                return node
            left = DFS(node.left, p, q)
            right = DFS(node.right, p, q)
            if not left: return right
            if not right: return left
            return node
        return DFS(root, p, q)
            
