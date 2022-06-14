#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        k = 0
        p1 = 0
        length = len(nums) 
        
        #arr is sorted, so use 2 pointers p1 and i
        #p1 is fast, i slow
        #when nums[i] == nums[p1], increment p1 by 1 to skip duplicate
        #when they are not equal, duplicate run has ended so copy value to nums[p1+1], 
        #then increment p1 until i reaches end of array
        for i in range(length):
            if nums[i] != nums[p1]:
                p1 += 1
                nums[p1] = nums[i]
        
        return p1 +1
            
            
        
            
