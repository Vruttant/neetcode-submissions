from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap_s = defaultdict(int)
        hashmap_t = defaultdict(int)

        for i in range(len(s)):
            hashmap_s[s[i]] += 1 
            hashmap_t[t[i]] += 1
        
        for key, value in hashmap_s.items():
            if hashmap_t.get(key) is None or hashmap_t.get(key) != hashmap_s.get(key):
                return False
        
        return True
