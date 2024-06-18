class Solution:
    def trimMean(self, arr: List[int]) -> float:
        sorted_arr = sorted(arr)
        five_percent = int(len(arr)*0.05)
        arr_len = len(arr)
        ans_arr = sorted_arr[five_percent:arr_len-five_percent]
        return sum(ans_arr) / len(ans_arr)
