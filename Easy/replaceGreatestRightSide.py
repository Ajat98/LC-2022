#https://leetcode.com/explore/featured/card/fun-with-arrays/511/in-place-operations/3259/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        highest = -1
        n = len(arr)
        
        #temp val is required since we are only comparing highest to the right
        for i in range(n-1, -1, -1):
            temp = arr[i]
            arr[i] = highest
            
            if temp > highest:
                highest = temp
                
        
        return arr
            
