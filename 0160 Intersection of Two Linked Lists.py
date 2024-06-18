class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        while (a and b):
            if a == b: return a
            a = a.next
            b = b.next
            if not a and not b: return None
            if not a: a = headB
            if not b: b = headA
        return None
