#https://leetcode.com/explore/featured/card/fun-with-arrays/511/in-place-operations/3260/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        #In place solution
        i = 0
        j = len(nums)-1
        
        while i < j:
            #j even, i odd, switch places
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]
            
            #Now check if positions of i and j meet array criterio, if they do, shrink boundaries by 1
            if nums[i] % 2 == 0: 
                i += 1
            if nums[j] % 2 != 0:
                j -= 1
                
        return nums
                
            
        
        #Join two sorted
        #return ( [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0])
    
        #Concise solution, slower runtime
        #nums.sort(key = lambda x: x % 2)
        #return nums
            
