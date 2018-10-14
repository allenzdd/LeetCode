# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
        


if __name__ == "__main__":
    root = TreeNode(3)
    root.left, root.right = TreeNode(9), TreeNode(20)
    root.right.left, root.right.right = TreeNode(15), TreeNode(7)
    res = Solution().mergeTrees(root, root)
    print(res)
