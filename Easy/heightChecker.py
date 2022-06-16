#https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3228/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        x = sorted(heights)
        
        errors = 0
        
        for i in range(len(heights)):
            if heights[i] != x[i]:
                errors += 1
        
        return errors
