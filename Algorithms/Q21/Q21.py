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

def merge(l1, l2):
    cur_head = l1
    while cur_head.next is not None:
        cur_head = cur_head.next
    cur_head.next = l2
    return l1

# iterative
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        cur = res
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return res.next

# recursive
class Solution2:
    def mergeTwoLists(self, l1, l2):
        # recursive must return
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

if __name__ == "__main__":
    head = ListNode(1)
    head.append(2)
    head.append(3)
    print(head)
    head2 = ListNode(1)
    head2.append(3)
    head2.append(4)
    print(head2)
    res = Solution2().mergeTwoLists(head, head2)
    print(res)