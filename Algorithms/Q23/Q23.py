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

def append_lst_ListNode(lst):
    head = ListNode(lst[0])
    for x in lst[1:]:
        head.append(x)
    return head

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        # merge left and right list node
        dummy = ListNode(0)
        cur = dummy
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        if right:
            cur.next = right
        return dummy.next

if __name__ == "__main__":
    l1 = append_lst_ListNode([1,4,5])
    l2 = append_lst_ListNode([1,3,4])
    l3 = append_lst_ListNode([2,6])
    lst = [l1, l2, l3]
    print(lst)
    res = Solution().mergeKLists(lst)
    print(res)

