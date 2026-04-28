class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(left, right, s):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True

        start = 0 
        end = len(s) - 1

        while start < end:
            
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return check_palindrome(start + 1, end, s) or check_palindrome(start, end - 1, s)
                    
        return True