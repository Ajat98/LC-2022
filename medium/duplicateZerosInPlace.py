class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        dupes = 0
        length = len(arr) -1
        
        #find num of zeroes to be duplicated
        for i in range(length):
            #stop when beyond last element in original list, which would be part of modified list
            if i > length - dupes:
                break
            
            #count zeroes
            if arr[i] == 0:
                #edge case where zero can't be duplicated, no more space
                #since i is on last element which would be included
                if i == length - dupes:
                    arr[length] = 0  #copy this zero without duplicaiton since at end of array size
                    length -= 1
                    break
                    
                dupes += 1
                
        #Now start at last element which is included in new list, work backwards
        end = length - dupes
        
        #copy zeroes twice, non zeroes once
        for i in range(end, -1, -1):
            
            #copy two zeroes, decrement dupes so we add zero to the left index
            if arr[i] == 0:
                arr[i+dupes] = 0
                dupes-=1
                arr[i+dupes] = 0
            else:
                arr[i + dupes] = arr[i]
                
                
                
#If not modifying in place, can use this approach
 s = 0
  d = 0

  # Copy is performed until the destination array is full.
  for s in range(N):
    if source[s] == 0:
      # Copy zero twice.
      destination[d] = 0
      d += 1
      destination[d] = 0
    else:
      destination[d] = source[s]

    d += 1
