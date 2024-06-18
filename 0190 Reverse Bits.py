class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = (bin(n))[2:][::-1] 
        ans_str = binary_str + "0"*(32-len(binary_str))
        ans = int(ans_str, 2)
        return ans
