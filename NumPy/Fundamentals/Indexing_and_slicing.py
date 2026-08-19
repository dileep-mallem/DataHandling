import numpy as np 

a=np.array([[10,20,30], # 0 , -3
            [40,50,60], #1 , -2
            [70,80,90]]) # 2'th row , -1

# Indexing Single Elemnts - [row,col]
print(a[1,2])
print(a[-1,-1])

# Row and Cols Slicing 
print(a[0])
print(a[:,1]) # entire Second Column 
print(a[:,-1]) # Enitre 3rd 

# Sub-Matrix Slicing [row_start:row_end, col_start:col_end]
print(a[0:2,1:3])
print(a[1:3,0:4]) 

print(a[:,:]) # All rows and Cols
print(a[:,0:2]) # all rows , first 2 cols 
print(a[:,::2]) # All Rows , every Second COl 
print(a[::-1])  # Rows Reversed 
print(a[:,::-1]) # Cols Reversed 

# Boolean Mask (Return Elements where  True )
mask=a>50 
print(mask) # Retturn matrix of True/False 
print(a[mask]) # Returns Elemnts Which satisfies 

# Assign Elemnts Through Slice - MODIFIES the Original (View !)
a[1,:]=0 # Second Row All cols Zeroes 
print(a) 
a[0:2,1]=0 # First 2 Two Rows , Second Col all Zeroes 
print(a)

# ** NumPy slices return views , not copies .Modifying a[0:2] modifies the original array. 
 
b=np.array([1,2,3,4,5])
c=b[0:4] # [1 2 3 4] (start , stop(exl) , step(not mand))
c+=1 # Increase +1 to all elemnts 
print(c) # [2 3 4 5]

print(b) # [ 2 3 4 5 5] (this array also change )

c=b[:4]
c-=1 # subtracts 1 from first 4 elements
print(b) # [1 2 3 4 5]

# To not modify , orignal array we should .copy() it 
c=b[:4].copy()
print(f" b : {b} c: {c}")
c+=1
print(f" b : {b} c: {c}") 

