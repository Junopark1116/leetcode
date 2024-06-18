class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brckts={'}':'{',')':'(',']':'['}
        for brckt in s:
            if brckt in brckts.values(): 
                stack.append(brckt)
            else:
                if stack and brckts[brckt]==stack[-1] :  
                    stack.pop()
                else: 
                    return False
        if stack:
            return False
        return True
