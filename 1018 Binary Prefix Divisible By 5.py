class Solution:
  def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
    ans = []
    cur = 0
    for num in nums:
      cur = (cur * 2 + num) % 5
      ans.append(cur % 5 == 0)
    return ans
