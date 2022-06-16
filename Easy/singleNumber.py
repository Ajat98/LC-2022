#https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1176/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        d = {}
        
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for x in d:
            if d[x] == 1:
                return x
            
        
