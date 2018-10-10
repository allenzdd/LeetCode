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

def list_append_listNode(lst):
    head = ListNode(lst[0])
    for x in lst[1:]:
        head.append(x)
    return head

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        res = dummy
        carry = 0
        while l1 or l2 or carry == 1:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            val += carry
            dummy.next = ListNode(val % 10)
            carry = int(val / 10)
            dummy = dummy.next
        return res.next


if __name__ == "__main__":
    l1 = list_append_listNode([2, 4, 3])
    l2 = list_append_listNode([5, 6, 4])
    print(l1)
    print('------------')
    print(l2)
    print('-------------')
    res = Solution().addTwoNumbers(l1, l2)
    print(res)

        