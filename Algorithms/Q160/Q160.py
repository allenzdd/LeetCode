# Definition for singly-linked list.
class ListNode(object):
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

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # init pointer current A and B
        curA, curB = headA, headB

        lenA = self.cal_length(curA)
        lenB = self.cal_length(curB)
        # restart pointer
        curA, curB = headA, headB
        
        if lenA > lenB:
            for _ in range(lenA - lenB):
                curA = curA.next
        elif lenB > lenA:
            for _ in range(lenB - lenA):
                curB = curB.next
        
        while curA != curB:
            curA = curA.next
            curB = curB.next
        return curA

    
    def cal_length(self, head):
        count = 0
        cur = head
        while cur:
            cur = cur.next
            count += 1
        return count
        


if __name__ == "__main__":
    hA = append_lst_to_ListNode([1,2,3,1])
    hB = append_lst_to_ListNode([5,4,2,3,1])
    res = Solution().getIntersectionNode(hA, hB)
    print(res)