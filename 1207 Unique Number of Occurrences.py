class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        value = Counter(arr).values()
        return True if sorted(value) == sorted(set(value)) else False
