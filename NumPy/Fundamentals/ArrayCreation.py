# Numpy are of Fixed Size Unlike Lists which are Dynamic 
# They have Same DType Elements 
# An Array Object is called ndArray in NumPy
# NumPy arrays can be defined using Python sequences such as lists and tuples. 
# a list of numbers will create a 1D array,
# a list of lists will create a 2D array,
# further nested lists will create higher-dimensional arrays

import numpy as np 

a1=np.array([1,2,3,4])
a2=np.array([[1,2,3],[4,5,6]],dtype=np.int16) # Signed Integer 16 bit ( raise OverFlowError )
a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(f"1D Array : {a1}")
print(f"2D ARray : \n{a2}")
print(a3D)


a = np.array([2, 3, 4], dtype=np.uint32)
b = np.array([5, 6, 7], dtype=np.uint32)
c_unsigned32 = a - b # Two same dt
print('unsigned c:', c_unsigned32, c_unsigned32.dtype) #unsigned c: [4294967293 4294967293 4294967293] uint32

c_signed32 = a - b.astype(np.int32) # diff , NumPy will assign a new type that satisfies all of the array elements involved in the computation, here uint32 and int32 can both be represented in as int64.
print('signed c:', c_signed32, c_signed32.dtype) # [ -3 -3 -3 ] int64 

print()

# Intrinsic NumPy array Creation

# NumPy has over 40 built-in functions for creating arrays as laid out in the Array creation routines. These functions can be split into roughly three categories, based on the dimension of the array they create:

# 1D arrays
# 2D arrays
# ndarrays

# 1D Array Creation ( .arange , .linspace)

# arange (start,stop(exl),step)

x1=np.arange(10) 
x2=np.arange(3,7)
x21=np.arange(3,9,dtype=np.float64) # [3. 4. 5. 6. 7. 8.]
x3=np.arange(1,2,0.1) # [1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9]
print(x1)
print(x2)
print(x21)
print(x3)

print()
# .linspace(start,stop(incl), no of Element req in that range)
l2=np.linspace(1,11,2) #[ 1. 11.]
l3=np.linspace(3,7,4) # [3.         4.33333333 5.66666667 7.        ]
print(l2)
print(l3)

print()

# 2D Array Creation (.eye , .diag , .vander)

# .eye(rows,cols) -> 1'sWhere i==j  rest all are 0's

e1=np.eye(3)
e2=np.eye(3,5)

print(e1)
print(e2)

# .diag() -> can define either a square 2D array with given values along the diagonal 
# or if given a 2D array returns a 1D array that is only the diagonal elements
# If v is a 2-D array, return a copy of its k-th diagonal. 
# If v is a 1-D array, return a 2-D array with v on the k-th diagonal.(rest all 0's)

d1=np.diag([[1,2],[3,4]]) # [1 4]
d2=np.diag([1,2,3])
print(d1)
print(d2)

d3=np.diag([1,2,3,4],2) # start assigning values after two elemnt (3rd element) in !st Row (Diaginal starts there ) , 
# and it fits all numbers ,return with extra 2 rows with all 0's 
print(d3)
#[[0 0 1 0 0 0]
#  [0 0 0 2 0 0]
#  [0 0 0 0 3 0]
#  [0 0 0 0 0 4]
#  [0 0 0 0 0 0]
#  [0 0 0 0 0 0]]
print(np.diag(d2)) # Extract Diagonal from d2 [1 2 3]
print()

# .vander(x,n) Vandermonde matrix 


# ndarray creation using .ones , .zeros((rows,cols)) and random 

n1=np.zeros((2,3))
n2=np.zeros((2,3,2)) # two 2-D matricies
print(n1)
print(n2)

# [[[0. 0.]
#   [0. 0.]
#   [0. 0.]]

#  [[0. 0.]
#   [0. 0.]
#   [0. 0.]]]

o1=np.ones((2,3))
o2=np.ones((2,3,2))
print(o1)
print(o2)

# _like variants — match another array's shape
np.zeros_like(n2)           # same shape as a2, all zeros
np.ones_like(o2)            # same shape as a2, all ones
# random 
# numpy.indices 


# Full  
f1=np.full((2,3),25,dtype=int) # full(shape,fillValue(Scalar or List),dtype)
print(f1)
f2=np.full((2,3),[5],dtype=int) 
print(f2)
# [[5 5 5]
#  [5 5 5]]
