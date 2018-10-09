# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
    def append(self, val):
        cur_node = self
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = ListNode(val)
    def traverse(self):
        cur_node = self
        while cur_node is not None:
            print(cur_node.val)
            cur_node = cur_node.next

# iterative
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev

# recursive
class Solution2:
    def reverseList(self, head, prev=None):
        if not head:
            return prev
        next_list_node = head.next
        head.next = prev
        return self.reverseList(next_list_node, head)


if __name__ == "__main__":
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    head.append(5)
    # head.traverse()
    print(head)
    print('--------------')
    res = Solution().reverseList(head)
    # res.traverse()
    print(res)
    print('----------------')
    # res2 = Solution2().reverseList(head)
    print(head)
    res