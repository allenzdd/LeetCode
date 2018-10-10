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
    def search(self, val):
        cur = self
        index = 0
        while val is not None:
            index += 1
            if cur.val == val:
                return index
            cur = cur.next
        return False

def list_append_listNode(lst):
    head = ListNode(lst[0])
    for x in lst[1:]:
        head.append(x)
    return head


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        
        for _ in range(n):
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next

if __name__ == "__main__":
    head = list_append_listNode([1,2,5,4,3])
    print(head)
    print('-------------')
    res = Solution().removeNthFromEnd(head, 2)
    print(res)
