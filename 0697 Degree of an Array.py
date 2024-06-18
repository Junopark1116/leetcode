class Solution:
  def findShortestSubArray(self, nums: List[int]) -> int:
    ans = 0
    deg = 0
    deb = {}
    count = collections.Counter()
    for i, num in enumerate(nums):
      deb.setdefault(num, i)
      count[num] += 1
      if count[num] > deg:
        deg = count[num]
        ans = i - deb[num] + 1
      elif count[num] == deg:
        ans = min(ans, i - deb[num] + 1)
    return ans
