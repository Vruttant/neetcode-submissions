class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = [] 

        word1_ptr = 0 
        word2_ptr = 0 

        while word1_ptr < len(word1) and word2_ptr < len(word2):
            result.append(word1[word1_ptr])
            result.append(word2[word2_ptr])
            word1_ptr += 1
            word2_ptr += 1

        
        while word1_ptr < len(word1):
            result.append(word1[word1_ptr])
            word1_ptr += 1

        while word2_ptr < len(word2):
            result.append(word2[word2_ptr])
            word2_ptr += 1

            
        res_string = "".join(result)

        return res_string
