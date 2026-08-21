import numpy as np 
import time

# Vectorization means replacing explicit Python loops with NumPy operations that run in compiled C code.
#  This is the single biggest performance lever in NumPy.

n=1_000_000
a=np.random.randn(n)

# Python loop 
t0=time.time()
result=0
for x in a :
    result+= x**2 
print(f"Loop : {time.time()-t0:.4f}s") #

# NumPy Vectorization 
result=np.sum(a**2)
print(f"NumPy: {time.time()-t0:.4f}s")  # (150× faster)


# Practical Vrctorization Patterns 

# Euclidean distance between two vectors 
p=np.array([1,2,3])
q=np.array([4,6,3])

dist = np.sqrt(np.sum((p-q)**2)) # la.norm(p-q)

print(dist)

# softmax fn - vectorized 
def softmax(x) :
    e_x = np.exp(x-np.max(x)) # subtract max for numerical stability
    return e_x // e_x.sum()
print(softmax(p)) # [0. 0. 0.]

# ReLU -> Vectorized 
relu = lambda x : np.maximum(0,x)
print(relu) #<function <lambda> at 0x7cc432d024d0>

