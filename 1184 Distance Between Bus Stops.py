class Solution:
  def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
    clock = 0
    counter = 0
    if start > destination:
      start, destination = destination, start
    for i, d in enumerate(distance):
      if i >= start and i < destination:
        clock += d
      else:
        counter += d
    return min(clock, counter)
