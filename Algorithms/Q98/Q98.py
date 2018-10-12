# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root, min_val=float('-inf'), max_val=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val >= max_val or root.val <= min_val:
            return False
        return self.isValidBST(root.left, min_val=min_val, max_val=root.val) and \
            self.isValidBST(root.right, min_val=root.val, max_val=max_val)


if __name__ == "__main__":
    root = TreeNode(2)
    root.left, root.right = TreeNode(1), TreeNode(3)
    print(Solution().isValidBST(root))
    root2 = TreeNode(5)
    root2.left, root2.right = TreeNode(1), TreeNode(4)
    root2.right.left, root2.right.right = TreeNode(3), TreeNode(6)
    print(Solution().isValidBST(root2))