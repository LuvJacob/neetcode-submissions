# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy


        #carry value if more than 9
        carry = 0
        #while either list still has numbers
        while l1 or l2 or carry:
            # get the curr values from l1 and l2 if not 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0


            # add them plus carry
            val = v1 + v2 + carry
            # find out if carry
            carry = val // 10
            # if carry get ones digit
            val = val % 10
            # add to dummy node
            curr.next = ListNode(val)

            # go to next pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
            
            