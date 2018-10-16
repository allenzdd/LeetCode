# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 

        # invert
        root.right, root.left = root.left, root.right

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root


if __name__ == "__main__":
    root = TreeNode(4)
    root.left, root.right = TreeNode(2), TreeNode(7)
    root.left.left, root.left.right = TreeNode(1), TreeNode(3)
    root.right.left, root.right.right = TreeNode(6), TreeNode(9)
    res = Solution().invertTree(root)
    print(res.left.left.val)