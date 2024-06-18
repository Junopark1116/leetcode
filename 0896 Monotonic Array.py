class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        reverse_flag = False
        if max(A) == A[0]:
            reverse_flag = True
        sorted_A = sorted(A, reverse=reverse_flag)
        if sorted_A == A:
            return True
        return False
