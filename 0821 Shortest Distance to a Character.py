class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        s_list = list(S)
        idx_list = []
        for i in range(len(s_list)):
            if s_list[i] == C:
                idx_list.append(i)
        ans_list = []
        for i in range(len(s_list)):
            temp = min([ abs(i-idx) for idx in idx_list ])
            ans_list.append(temp)
        return ans_list
