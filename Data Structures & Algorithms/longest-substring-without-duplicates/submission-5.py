class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0 

        if len(s) <= 1: 
            return 1 

        i, j = 0, 0 
        max_len = 0
        visited = set()
        while j <= len(s) - 1: 
            if s[j] in visited:
                visited.remove(s[i]) 
                i += 1
            else:
                visited.add(s[j])
                max_len = max(max_len, len(visited)) 
                j += 1

        return max_len




            
