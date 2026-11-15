# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        curr = head
        a = []
        while curr:
            a.append(curr.val)
            curr = curr.next
            
        max_sum = 0
        n = len(a)
        for i in range(n // 2):
            current_sum = a[i] + a[n - 1 - i]
            if current_sum > max_sum:
                max_sum = current_sum
                
        return max_sum