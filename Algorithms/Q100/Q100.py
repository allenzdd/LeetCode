# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 36 ms
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: return True
        if not p or not q:  return False
        if p.val != q.val:  return False
        return self.isSameTree(p.left, q.left) and \
                self.isSameTree(p.right, q.right)

# 44 ms
class Solution2:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p or not q:
            return p == q
        return p.val == q.val and self.isSameTree(p.left, q.left) \
                and self.isSameTree(p.right, q.right)

        

if __name__ == "__main__":
    root = TreeNode(3)
    root.left, root.right = TreeNode(9), TreeNode(20)
    root.right.left, root.right.left = TreeNode(15), TreeNode(7)

    root2 = TreeNode(3)
    root2.left, root2.right = TreeNode(9), TreeNode(20)
    root2.right.left, root2.right.left = TreeNode(15), TreeNode(7)

    print(Solution2().isSameTree(root, root2))
