# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
        return False        
    
# this is the best approach  
# it uses fast-slow technique (floyd cycle test) to check if there is a loop
# the point is fast and slow pointers chase each other till they meet.

# time complexity - O(n) --> we must loop trough entire list +1 to reach a same node, if there is no loop then we see fast reaching null first and we return false.
# Space complexity - O(1) --> as we are not using any separate datastructure to store.

# See other commits for other solutions