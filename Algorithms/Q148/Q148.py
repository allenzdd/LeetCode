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
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge_sort(left,right)
    
    def merge_sort(self, left, right):
        dummy = cur = ListNode(0)
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        cur.next = left or right
        return dummy.next


if __name__ == "__main__":
    head = append_lst_to_ListNode([1,3,2,5,4])
    print(head)
    res = Solution().sortList(head)
    print(res)