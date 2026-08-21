import numpy as np 

a=np.array([3,1,4,1,5,9,2,0,6])

# Sorting 
print(np.sort(a))

#* a.sort() , Inplace sort -> Modifoes 'a'
print(np.sort(a)[::-1]) # Descending 

# 2-D Sort 
m=np.array([[3,1],[4,2]])

print(np.sort(m,axis=0)) # sort down columns:
print(np.sort(m,axis=1)) # sort each row 

# arg sort  - indices that would sort 
a=np.array([30,10,20])
idx=np.argsort(a) # [1 2 0 ] - index 1 has smallest value
print(idx,a[idx]) # [10 20 30] — sorted using fancy indexing

# searching 
a=np.array([1,5,3,8,2])
print(np.where(a>3)) # (array([1, 3]),)  — indices where condition true
print(np.searchsorted([1,3,5],4))  # 2  — insertion point in sorted array
print(np.nonzero(a)) # (array([0, 1, 2, 3, 4]),) ->  indices of non-zero elements