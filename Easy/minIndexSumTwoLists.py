#https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1177/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        d = {}
        res = []
        
        for i in range(len(list1)):
            if list1[i] in list2:
                word = list1[i]
                d[word] = i
                #print(d)
            
        for i in range(len(list2)):
            if list2[i] in list1:
                word = list2[i]
                if word in d:
                    d[word] += i
                else:
                    d[word] = i
                #print(d)
                
        x = min(d.values())
        
        for i in d.keys():
            if d[i] == x:
                res.append(i)
        
        return res
