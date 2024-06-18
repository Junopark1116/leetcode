class Solution:
  def canThreePartsEqualSum(self, arr: List[int]) -> bool:
    summ = sum(arr)
    if summ % 3 != 0:
      return False
    average = summ // 3
    ptCount = 0
    ptSum = 0
    for a in arr:
      ptSum += a
      if ptSum == average:
        ptCount += 1
        ptSum = 0
    return ptCount >= 3
