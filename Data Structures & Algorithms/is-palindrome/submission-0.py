import string 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_wo_spaces = list("".join(s.split(" ")).lower())

        for ch in string_wo_spaces:
            if ch in string.punctuation:
                string_wo_spaces.remove(ch)
                
        string_wo_spaces = "".join(string_wo_spaces)

        start = 0 
        end = len(string_wo_spaces) - 1 

        while start < end: 
            if string_wo_spaces[start] == string_wo_spaces[end]:
                start += 1
                end -= 1
                continue 
            else:
                return False 
    
        return True
