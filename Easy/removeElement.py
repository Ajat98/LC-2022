https://leetcode.com/explore/featured/card/fun-with-arrays/526/deleting-items-from-an-array/3247/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        
        length = len(nums) -1
        p1 = length #start at end of array
        temp = 0
     
        for i in range(length, -1, -1): #must use -1 to include last element when going right-left
            if nums[i] == val:
                #temp = nums[i] #not needed here
                nums[i] = nums[p1]
                nums[p1] = 0
                p1 -= 1
                nums.pop()
