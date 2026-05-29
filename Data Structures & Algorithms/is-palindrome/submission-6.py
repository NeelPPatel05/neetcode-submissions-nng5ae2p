class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        result = ''.join(c for c in s.lower() if c.isalnum())
        right_point = len(result)-1
        left_point = 0
        
        while (right_point > left_point):    
            if(result[right_point] != result[left_point]):
                return False
            right_point -= 1
            left_point += 1
        return True
    


