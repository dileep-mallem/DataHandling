import numpy as np 

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])

#Concatenation 

print(np.concatenate([a,b],axis=0)) # Stack rows 
print(np.concatenate([a,b],axis=1)) # stack cols 

# stack - creates a new axis 

print(np.stack([a,b],axis=0))# shape (2,2,2) — new first axis
print(np.stack([a,b],axis=1)) # shape(2,2,2) -> new Second aix 

print(np.vstack([a,b])) # same as concatenate axis=0
print(np.hstack([a,b])) # same as concatenate axis=1

print()
# Spiltting 

x=np.arange(12)
print(x)

print(np.split(x,2))
x=x.reshape(4,3)
print(x)
print(np.split(x,(0,4),axis=0)) # def axis=0
print(np.vsplit(x,(2,3)))
print(np.hsplit(x,(2,3)))
print(np.array_split(x,3))