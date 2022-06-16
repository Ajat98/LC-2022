#https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3230/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      
      #Optimal Solution
        longest = 0
        zeros = 0
        left = 0
        right = 0
        
        while right < len(nums): #keep right side of sliding window inbounds
            if nums[right] == 0:
                zeros += 1
            
            while zeros == 2: #if two zeros, must contract window
                if nums[left] == 0:
                    zeros -= 1 #since we are moving the last zero out of window below
                left += 1
                
            longest = max(longest, right - left + 1)
            #expand window by 1 to the right
            right += 1
        return longest
        
#NOT a very time efficient solution, O(n^2)
#         longest = 0
#         count = 0 
#         zeros = 0
        
#         for i in range(len(nums)):
#             zeros = 0
#             for x in range(i, len(nums)): #iterate over sequences to the right of starting pos i
#                 if zeros == 2:
#                     break
#                 if nums[x] == 0:
#                     zeros += 1
#                 if zeros <= 1:
#                     longest = max(longest, x - i + 1) #longest sequence we encounter so far
                    
#         return longest
