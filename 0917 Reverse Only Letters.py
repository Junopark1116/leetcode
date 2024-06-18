class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        temp = []
        indexs = {} 
        ans = []
        cnt = 0
        s_list = list(S)
        for i in range(len(s_list)):
            if s_list[i].isalpha() == True:
                temp.append(s_list[i])
                cnt = cnt + 1
            if s_list[i].isalpha() == False:
                indexs[i] = s_list[i]
        if cnt == len(S):
            ans = S[::-1]
        else:
            keys = list(indexs.keys())
            temp = temp[::-1]
            idx = 0      
            for i in range(len(S)):
                if i in keys:
                    ans.append(indexs[i])
                elif i not in keys:
                    ans.append(temp[idx])
                    idx = idx + 1       
            ans = ''.join(ans)
        return ans
