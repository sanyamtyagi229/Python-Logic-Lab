# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode | None):
        self.head=head

    def getRandom(self) -> int:
        current = self.head
        res = current.val
        i = 1
        
        while current:
            if random.randint(1, i) == 1:
                res = current.val
            current = current.next
            i += 1
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()