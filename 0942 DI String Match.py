class Solution:
  def diStringMatch(self, s: str) -> List[int]:
    ans = []
    less = 0
    more = len(s)
    for c in s:
      if c == 'I':
        ans.append(less)
        less += 1
      else:
        ans.append(more)
        more -= 1
    return ans + [less]
