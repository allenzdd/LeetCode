# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, node, level):
        if not node:
            return
        if len(self.res) <= level:
            self.res.append([])
        self.res[level].append(node.val)
        self.dfs(node.left, level+1)
        self.dfs(node.right, level+1)



if __name__ == "__main__":
    root = TreeNode(3)
    root.left, root.right = TreeNode(9), TreeNode(20)
    root.right.left, root.right.left = TreeNode(15), TreeNode(7)
    res = Solution().levelOrder(root)
    print(res)

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#     def insert(self, val):
#         if self.root is None:
#             self.root = TreeNode(val)
#         else:
#             cur_node = self.root
#             while True:
#                 if val > cur_node.val:
#                     if cur_node.right is None:
#                         cur_node.right = TreeNode(val)
#                         break
#                     else:
#                         cur_node = cur_node.right
#                 elif val < cur_node.val:
#                     if cur_node.left is None:
#                         cur_node.left = TreeNode(val)
#                         break
#                     else:
#                         cur_node = cur_node.left
#                 else:
#                     break