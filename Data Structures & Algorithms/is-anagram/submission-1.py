from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Brute Force
        # str1 = "".join(sorted(s))
        # str2 = "".join(sorted(t))
        # print(str1)
        # print(str2)
        
        # if str1 == str2:
        #     return True
        
        # return False

        # Optimised solution
        s_counter = {}
        t_counter = {}

        for ch in s:
            s_counter[ch] = s_counter.get(ch, 0) + 1
        
        for ch in t:
            t_counter[ch] = t_counter.get(ch, 0) + 1

        print(s_counter)
        print(t_counter)

        if s_counter == t_counter:
            return True

        return False

