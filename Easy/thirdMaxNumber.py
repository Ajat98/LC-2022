#https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3231/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        a = set(nums) #get rid of duplicates
        b = list(a) #convert back to list
        
        if len(b) <= 2: #if len below 3, return max
            return max(b)
        
        else: 
            b.sort() #organize list in increasing order, return 3rd value from end of list
            return b[-3]
