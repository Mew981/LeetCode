# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        #iterate through A
        #iterate through B
        #find when A.next == B.next
        #then return A.next
        #how do u iterate through a singly linked list?
        if not headA or not headB:
            return None
        pA = headA
        pB = headB
        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
