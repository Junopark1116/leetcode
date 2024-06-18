class Solution:
  def calPoints(self, operations: List[str]) -> int:
    ans = []
    for operation in operations:
      match operation:
        case '+':
          ans.append(ans[-1] + ans[-2])
        case 'D':
          ans.append(ans[-1] * 2)
        case 'C':
          ans.pop()
        case default:
          ans.append(int(operation))
    return sum(ans)
