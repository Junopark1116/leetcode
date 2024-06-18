from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        array = A.split(" ") + B.split(" ")
        cnt = list(Counter(array).items())
        ans = [item[0] for item in cnt if item[1] == 1]
        return ans
