# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')
        self.dfs(root)
        return self.res
        
    def dfs(self, node):
        if not node:
            return 0
        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))
        self.res = max(self.res, left+right+node.val)
        return max(left, right) + node.val

if __name__ == "__main__":
    root = TreeNode(-10)
    root.left, root.right = TreeNode(9), TreeNode(20)
    root.right.left, root.right.right = TreeNode(15), TreeNode(7)
    # root = TreeNode(2)
    # root.left = TreeNode(-1)
    res = Solution().maxPathSum(root)
    print(res)