class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        test1 = sorted(s)
        test2 = sorted(t)
        if(test1 == test2):
            return True
        return False


        