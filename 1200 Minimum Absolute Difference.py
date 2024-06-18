class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arrSorted = sorted(arr)
        ans = []
        mini = arrSorted[-1] - arrSorted[0]
        for n in range(len(arr)-1):
            mini = min(mini, arrSorted[n+1] - arrSorted[n])
        for n in range(len(arr)-1):
            if arrSorted[n+1] - arrSorted[n] == mini:
                ans.append([arrSorted[n], arrSorted[n+1]])   
        return ans
