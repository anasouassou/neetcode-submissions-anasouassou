# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode(0)
        current = dummy
        current_L1, current_L2 = list1, list2

        while current_L1 and current_L2:
            if current_L1.val < current_L2.val:
                current.next = ListNode(current_L1.val)
                current_L1 = current_L1.next
            else: 
                current.next = ListNode(current_L2.val)
                current_L2 = current_L2.next
            current = current.next

        current.next = current_L1 if current_L1 else current_L2    
        
        return dummy.next


