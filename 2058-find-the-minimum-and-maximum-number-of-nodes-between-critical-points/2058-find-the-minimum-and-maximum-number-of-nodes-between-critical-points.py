# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
            
        first_cp = -1
        last_cp = -1
        min_dist = float('inf')
        
        idx = 1
        prev = head
        curr = head.next
        
        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                
                if first_cp == -1:
                    first_cp = idx
                else:
                    min_dist = min(min_dist, idx - last_cp)
                
                last_cp = idx
                
            prev = curr
            curr = curr.next
            idx += 1
            
        if first_cp != -1 and first_cp != last_cp:
            return [min_dist, last_cp - first_cp]
        else:
            return [-1, -1]