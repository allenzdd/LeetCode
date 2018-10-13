# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        self.LP(root)
        return self.diameter

    def LP(self, node):
        if not node:
            return 0
        left = self.LP(node.left)
        right = self.LP(node.right)
        self.diameter = max(self.diameter, left+right)
        return max(left, right) + 1
        


if __name__ == "__main__":
    root = TreeNode(3)
    root.left, root.right = TreeNode(9), TreeNode(20)
    root.right.left, root.right.right = TreeNode(15), TreeNode(7)
    res = Solution().diameterOfBinaryTree(root)
    print(res)
