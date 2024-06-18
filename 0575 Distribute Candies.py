class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
            candyType.sort()
            num = int(len(candyType)/2)
            count = 1
            for i in range(len(candyType)-1):
                if candyType[i] != candyType[i+1]:
                    count+=1
            return num if count> num  else count
