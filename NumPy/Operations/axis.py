import numpy as np 

# axis = N means " Collapse along Dim N " -> dim N disappears form the Output Shape

a=np.array([[1,2,3],
            [4,5,6]]) # shape(2,3)

# sxis=0 (Column-wise): Collapses the rows. It looks down each column.
# axis=1 (Row-wise): Collapses the columns. It looks across each row. 

print(np.sum(a,axis=0)) # (3,) rows collapsed -> [5 7 9]  sum down the cols 
print(np.sum(a,axis=1)) # (2,) cols collapsed -> [6 15] sum acr0ss the rows

# keepdims=True -> preserve dimension for broadcasting 
print(np.sum(a,axis=1,keepdims=True)) # shape(2,1) -> : [[6],[15]]

# 3D : shape(2,3,4)
b=np.random.randn(2,3,4)

print((np.sum(b,axis=0)).shape) # (3,4) -> first dim collapsed
print((np.sum(b,axis=1)).shape) # (2,4) -> Second dim collapsed
print((np.sum(b,axis=2)).shape) # (2,3) -> Third dim collapsed
print((np.sum(b,axis=(0,1))).shape) # (4,) -> first and second dim's collapsed