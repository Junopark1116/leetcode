class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.kth = sorted(nums, reverse=True)[:k]
    def add(self, val: int) -> int:
        self.kth.append(val)
        self.kth = sorted(self.kth, reverse=True)[:self.k]
        return self.kth[-1]
