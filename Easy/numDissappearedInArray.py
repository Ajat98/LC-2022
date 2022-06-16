#https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3270/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        d = {}
        
        #fill hashtable with all numbers in array
        for i in nums:
            d[i] = 1
        
        #will hold numbers not in array
        a = []
        
        #since 1, n is in range of array, search for numbers starting at 1 and up to the end of the array
        #need to specify 1 starting, and + 1 to length of array due to range syntax
        for i in range(1, len(nums)+1):
            if i not in d:
                a.append(i)
                
        return a
                
        
