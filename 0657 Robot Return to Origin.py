from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt = dict(Counter(moves))    
        cnt_keys = list(cnt.keys())
        pairs = [ {"L", "R"}, {"U", "D"}, {"L", "R", "U", "D"} ] 
        if set(cnt_keys) not in pairs:
            return False
        else:
            if set(cnt_keys) == pairs[0]:
                if cnt['L'] != cnt['R']:
                    return False
            elif set(cnt_keys) == pairs[1]:
                if cnt['U'] != cnt['D']:
                    return False
            elif set(cnt_keys) == pairs[2]:
                if (cnt['L'] != cnt['R']) or (cnt['U'] != cnt['D']):
                    return False          
        return True
