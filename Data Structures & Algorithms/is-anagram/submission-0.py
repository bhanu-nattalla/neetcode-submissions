class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = "".join(sorted(s))
        str2 = "".join(sorted(t))
        print(str1)
        print(str2)
        
        if str1 == str2:
            return True
        
        return False