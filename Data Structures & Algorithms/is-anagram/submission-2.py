class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count_tracker = {}

        for s_char in s:
            if s_char in s_count_tracker:
                s_count_tracker[s_char] += 1
            else:
                s_count_tracker[s_char] = 1

        
        for t_char in t:
            if t_char not in s_count_tracker:
                return False
            else:
                s_count_tracker[t_char] -= 1
                if s_count_tracker[t_char] < 0:
                    return False
        
        return True