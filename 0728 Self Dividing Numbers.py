class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = [num for num in range(left, right+1) if '0' not in str(num) and all([num % int(n) == 0 for n in str(num)])]
        return ans
