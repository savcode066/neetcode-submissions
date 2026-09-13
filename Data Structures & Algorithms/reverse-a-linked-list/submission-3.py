# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev_ptr = None
        while temp:
            next_ptr = temp.next
            temp.next = prev_ptr
            prev_ptr = temp
            if not next_ptr:
                break
            temp = next_ptr
        return temp
            
        