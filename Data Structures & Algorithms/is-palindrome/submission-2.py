from string import punctuation
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove spaces 
        s = "".join(s.split(" "))
        start = 0 
        end = len(s) - 1

        while start < end: 
            if s[start] in punctuation:
                start += 1
                continue
        
            if s[end] in punctuation:
                end -= 1
                continue
                
            if s[start].lower() != s[end].lower():
                return False 
            
            start += 1
            end -= 1
            
        return True 