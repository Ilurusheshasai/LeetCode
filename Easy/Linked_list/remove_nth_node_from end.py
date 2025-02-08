# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize two pointers
        first = head
        second = head
        
        # Move first pointer n steps ahead
        for _ in range(n):
            first = first.next
        
        # Handle case where n is equal to the length of the list
        if not first:
            return head.next
        
        # Move both pointers until first reaches the end
        while first.next:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        second.next = second.next.next
        
        return head