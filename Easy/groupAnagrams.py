#https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1124/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        
        #sort strings then add the sorted string into hash table with unsorted string in array as val
        #if sorted string already in table, append the current string to the value list
        for i in range(len(strs)):
            w = strs[i]
            s = "".join(sorted(w))
            if s in d:
                d[s].append(w)
            else:
                d[s] = [w]
        
        return [x for x in d.values()]
        #print(d)
