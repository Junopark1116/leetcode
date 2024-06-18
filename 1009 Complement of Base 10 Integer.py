class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int("".join(list(map(str, [1-num for num in list(map(int, list(str(bin(N))[2:])))]))), 2)
