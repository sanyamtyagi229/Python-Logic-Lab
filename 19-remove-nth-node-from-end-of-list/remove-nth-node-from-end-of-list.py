# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        c=0
        while temp!=None:
            temp=temp.next
            c=c+1
        if n == c:
            return head.next
        t=head
        for i in range(c - n - 1):
            t = t.next
        t.next=t.next.next
        return head
        