class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_que, t_que = deque(s), deque(t)
        s_stack, t_stack = [], []
        while s_que:
            s1 = s_que.popleft()
            if s1!='#':
                s_stack.append(s1)
            else:
                if len(s_stack)!=0:
                    s_stack.pop()
        while t_que:
            t1 = t_que.popleft()
            if t1!='#':
                t_stack.append(t1)
            else:
                if len(t_stack)!=0:
                    t_stack.pop()
        return True if s_stack==t_stack else False
