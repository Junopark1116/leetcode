class Solution:
  def numberOfLines(self, widths: List[int], s: str) -> List[int]:
    numLines = 1
    runWidth = 0
    for c in s:
      width = widths[ord(c) - ord('a')]
      if runWidth + width <= 100:
        runWidth += width
      else:
        numLines += 1
        runWidth = width
    return [numLines, runWidth]
