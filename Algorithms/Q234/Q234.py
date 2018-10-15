# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
    def append(self, x):
        cur = self
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(x)

def append_lst_to_ListNode(lst):
    head = ListNode(lst[0])
    for x in lst[1:]:
        head.append(x)
    return head

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse right list node
        prev = None
        while slow:
            cur = slow.next
            slow.next = prev
            prev = slow
            slow = cur
        
        # judge equal
        tail = prev
        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True


if __name__ == "__main__":
    head = append_lst_to_ListNode([1,2,3,2,1])
    print(head)
    print(Solution().isPalindrome(head))