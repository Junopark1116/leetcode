class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ans = False 
        valid = False 
        n = len(arr) 
        i = 0 
        while i + 1 < n and arr[i] < arr[i+1]: 
            i += 1 
            valid = True 
        while i + 1 < n and arr[i] > arr[i+1] and valid == True: 
            i += 1 
            ans = True 
        if i+1 != n :
            ans = False
        return ans
