#https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1115/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         d = {}
        
         for i,x in enumerate(nums):
                
                #if this number is already in d, the current index and index of the number in d is our answer
                k = target - x

                #check d key values for k, if found return index of current val and index of k
                if k in d:
                    return [d[k], i]
                
                #store current val in d with corresponding index
                else:
                    d[x] = i #must use number value as the key
