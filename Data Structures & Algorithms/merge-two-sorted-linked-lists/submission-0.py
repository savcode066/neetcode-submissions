# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None
        
        new_ll = ListNode()
        ans = new_ll

        temp_1 = list1
        temp_2 = list2

        while temp_1 or temp_2:
            if not temp_1:
                new_ll.next = temp_2
                temp_2 = temp_2.next
            elif not temp_2:
                new_ll.next = temp_1
                temp_1 = temp_1.next
            else:
                if temp_1.val < temp_2.val:
                    new_ll.next = temp_1
                    temp_1 = temp_1.next
                else:
                    new_ll.next = temp_2
                    temp_2 = temp_2.next

            new_ll = new_ll.next


        return ans.next
        
