# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """


head = [1, 2, 3, 4, 5]
n = 2

res = Solution().removeNthFromEnd(head, n)

print(res)
