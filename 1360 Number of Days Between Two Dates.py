import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date_01 = datetime.datetime.strptime(date1, '%Y-%m-%d')
        date_02 = datetime.datetime.strptime(date2, '%Y-%m-%d')
        ans = abs(date_01- date_02).days
        return ans
