import numpy as np 

a=np.arange(12)

# reshape - total elements Must stay the Same 
b=a.reshape(3,4) # 3 roes , 4 cols  - shape(3,4) return View if Possible , else raises ValueError
c=a.reshape(2,3,2) 
d=a.reshape(3,-1) # -1 means "infer" → shape (3, 4) 12//3 -> 4 cols 
# When you pass 3 as the first dimension and -1 as the second, 
# NumPy divides the total number of elements by 3 to determine how many columns are needed to make the reshape work.

print( f" a : \n {a} \n b : \n {b}  \nc :\n {c} \n d : \n{d}")

# faltten vs ravel 
print(b.flatten())  # always returns COPY, shape (12,)
print(b.ravel())  # returns VIEW if possible, shape (12,)

# Transpose 1.a.T 2.np.transpose(a,axis=(optional))
print(f" b : {b} \n Its Tranpose : \n {b.T}\n ")
print(c)
print(np.transpose(c,(1,0,2))) # specify exact axis order , axis 1 to fromt , 0 to middle and 3 to back 
a=np.array([[1,2,3],[4,5,6]])
print(np.transpose(a))

# Adding and Removing Dimensions 
a=np.array([1,2,3]) # Shape(3,)
# Add a row dimension (makes it a 2D row vector)
print(a,a[np.newaxis,:],a[np.newaxis,:].shape) # (1,3) -> row vector
# Add a colum dimension (makes it a 2D col vector)
print(a,a[:,np.newaxis],a[:,np.newaxis].shape) # (3,1) -> col vector
# Add an axis at index 0 (front)
print(a,np.expand_dims(a,0),np.expand_dims(a,0).shape) # (1,3)
# Add an axis at index 1 (end)
print(a,np.expand_dims(a,1),np.expand_dims(a,1).shape) # (3,1)
# Remove all size-1 dimensions
print(a,np.squeeze(a[np.newaxis]),np.squeeze(a[np.newaxis]).shape) # (3,) — remove size-1 axes


# None is an alias for np.newaxis
b=a[:,None] 
print(b) # shape : (3,1)
