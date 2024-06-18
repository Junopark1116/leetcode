class Solution:
  def addToArrayForm(self, num: List[int], k: int) -> List[int]:
    for i in reversed(range(len(num))):
      k, num[i] = divmod(num[i] + k, 10)
    while k > 0:
      num = [k % 10] + num
      k //= 10
    return num
