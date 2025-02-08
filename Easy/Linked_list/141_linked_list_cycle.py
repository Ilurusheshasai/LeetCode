# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        while head:
            if head not in seen:
                seen.add(head)
                head = head.next
            else:
                return True
        return False
    
# this is one of the approach this 
# it uses hashing technique to store the address of the node
# the point is when we reach the same node again next time signifes the point that we are in a loop, we can find the adress in the hash set.
# this way we can identify the cycle.

# time complexity - O(n) --> we must loop trough entire list +1 to reach a same node, if there is no loop them we see null and we return false.
# Space complexity - O(n) --> as we are using a separate set to store the addresses of the elements