class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = head
        def solve(rt):
            if rt : 
                if rt.next != None and rt.val == rt.next.val : 
                    rt.next = rt.next.next
                    solve(rt)
                else:
                    solve(rt.next)
        solve(head)
        return res
