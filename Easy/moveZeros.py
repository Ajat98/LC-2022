#https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        posLastZero = 0 #track index of last zero
        n = len(nums)
        temp = 0
        
        #iterate across, tracking all non zero elements
        #If found a nonzero elem, we change the last index we found a zero at to the current number,
        #then increment poslastzero by + 1
        for i in range(n):
            if nums[i] != 0:
                nums[posLastZero] = nums[i]
                posLastZero += 1
        
        #Finally, we know how many zeros to add to end of array
        #Start at end of array, replace amount of zeros found
        for i in range(n-1, posLastZero-1, -1):
            print(nums[i])
            nums[i] = 0
