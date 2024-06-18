class MyHashSet:
    def __init__(self):
        self.hash = [0 for _ in range(1000001)]
    def add(self, key: int) -> None:
        self.hash[key] = 1
    def remove(self, key: int) -> None:
        self.hash[key] = 0
    def contains(self, key: int) -> bool:
        return True if self.hash[key] else False
