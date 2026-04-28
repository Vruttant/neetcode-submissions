class Solution:
    def giveCharMap(self, string):
        char_map = dict() 
        for char in string:
            if char_map.get(char):
                char_map[char] += 1
            else:
                char_map[char] = 1 
        
        return char_map 
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = dict() 
        t_map = dict() 
        
        return self.giveCharMap(s) == self.giveCharMap(t)
