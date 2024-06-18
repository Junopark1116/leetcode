class Solution:
    def mergeTwoLists(self, lst1: Optional[ListNode], lst2: Optional[ListNode]) -> Optional[ListNode]:
        if lst1 is None or lst2 is None:
            return lst1 or lst2
        if lst1.val < lst2.val :
            lst1.next = self.mergeTwoLists(lst1.next, lst2)
            return lst1
        else:
            lst2.next = self.mergeTwoLists(lst1, lst2.next)
            return lst2
