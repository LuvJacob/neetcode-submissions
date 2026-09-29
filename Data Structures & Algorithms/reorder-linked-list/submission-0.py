# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        n = 0
        while curr is not None:
            n+=1
            curr = curr.next
        curr = head
        for i in range((n+1)//2):
            prev = curr
            curr = curr.next
        prev.next = None
        second = curr
        prev_rev = None
        while second:
            nxt = second.next
            second.next = prev_rev
            prev_rev = second
            second = nxt
        second = prev_rev  # head of reversed second half
        first = head
        while second:
            fnext = first.next
            snext = second.next

            first.next = second
            second.next = fnext

            first = fnext  # safe for odd length
            second = snext
        return None

        
        
        