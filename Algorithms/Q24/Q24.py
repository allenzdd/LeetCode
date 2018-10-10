# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
    def append(self, val):
        cur = self
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(val)


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            cur.next = second
            first.next = second.next
            second.next = first
            cur = cur.next.next
        return dummy.next

# recursive
class Solution2:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_start)
        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    print(head)
    print('------------')
    res = Solution2().swapPairs(head)
    print(res)
