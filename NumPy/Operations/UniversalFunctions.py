import numpy as np 


# ufuncs are functions that operate element-wise on ndarrays, written in C for speed.
# They support broadcasting, type casting, and optional output arrays.

# Math ufuncs
# numpy.ufunc' object is not subscriptable
a=np.array([0,np.pi/2,np.pi])
print(a) # [0.         1.57079633 3.14159265]
s=np.sin(a)
print(s) #[0.0000000e+00 1.0000000e+00 1.2246468e-16]
c=np.cos(a)
print(c)
l=np.log([1,np.e,10]) 
e=np.exp([0,1,2])
print(l,e)

s=np.sqrt([4,16,64])
print(s)

ab=np.abs([-1,-2,90])
print(ab)

f=np.floor([1.7,11.2]) # .ceil([])
print(f)

r=np.round([1.4,1.5,1.7]) # [1. 2. 2.] (banker's Rounding)
print(r)

# comaparision ufuncs 
maximum=np.maximum([1,5,3],[4,2,6]) # [4 5 6] , [1 2 3] for np.minimum()
print(maximum) 

cl=np.clip([-1,5,12],0,10)  # [0 5 10] clamp to range ( if grater >10 -> 10 , <0 -> 0)
print(cl)

#out= parameter — write result into existing array (no copy)
result=np.empty(3)
print(result) # [     nan 2.5e-323 5.9e-323]
np.sqrt([4,9,16],out=result)
print(result) # [2 3 4]

