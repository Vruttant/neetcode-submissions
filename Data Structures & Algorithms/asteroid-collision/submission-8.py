class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = [] 

        for ast in asteroids: 
            if len(s) == 0:
                s.append(ast)
                continue 
            
            if (s[-1] > 0 and ast > 0 ) or (s[-1] < 0 and ast < 0):
                s.append(ast)
                continue 
            
            while s and s[-1] > 0 and ast < 0:
                if abs(ast) > s[-1]:
                    s.pop()
                    continue
                elif abs(ast) == s[-1]:
                    s.pop()
                    break
                else:
                    break
            else:
                s.append(ast)

        return s