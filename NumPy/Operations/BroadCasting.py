import numpy as np 

# BroadCasting -> allows numpy to operate on arrays of diff shapes (without extra copies)
# Numpy strceches smaller ones to match lasrger -> conceptually not in memeory 

# Rules :
# 1.Applies right to left ,
#  sizes must match or one must be 1 
# If neither , ValueError 

a=np.array([[1],[2],[3]]) # (3,1)
b=np.array([[10,20,30,40]]) # (1,4)

print(a+b,(a+b).shape) # (3,4)
# 11 21 31 41
# 12 22 32 42
# 13 23 33 43

# row-wise Normalization (N,D)->(N,1)
x=np.random.randn(5,3)
print(x) # shape(5,3)
x_mean=x.mean(axis=1,keepdims=True) # (5,1)
print(x_mean)
x_cenetered=x-x_mean  # broadcasts (5,3) - (5,1) → (5,3)
print(x_cenetered)

# add bias to each row in ML

w=np.random.randn(3,4)
print(w)
bias=np.array([1,2,3,4]) #(4,) broadcasts over rows
result=w+bias 
print(result) # (3,4)

# Broadcasting error example
# np.array([1,2,3]) + np.array([1,2]) → ValueError (3 vs 2, neither is 1)
