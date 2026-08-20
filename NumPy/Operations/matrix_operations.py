import numpy as np 
import numpy.linalg as la 

a=np.array([[2,1],
            [5,3]])

b=np.array([8,21])

# core Operations 
print(a@a)
print(a.T) # or np.transpose(a)
print(np.dot(a,a)) # same as @ ( as one of two os 2-D)

# np.dot()
# If both a and b are 1-D arrays, it is inner product of vectors (without complex conjugation).
# If both a and b are 2-D arrays, it is matrix multiplication, but using matmul or a @ b is preferred.
# If either a or b is 0-D (scalar), it is equivalent to multiply and using numpy.multiply(a, b) or a * b is preferred.

# numpy.linalg

print(la.det(a)) # deteminant
print(la.inv(a)) # inverse
print(la.solve(a,b)) # solve Ax = b  (better than inv @ b)
print(la.norm(a)) # 6.244997998398398 #* Frobenius norm (default)
print(la.norm(b,ord=2))  # L2 norm of vector
print(la.matrix_rank(a)) # 2 matrix rank 
print(la.trace(a)) # sum of trace elemets

print()

# Eigen Values and vectors 
vals,vecs=la.eig(a) # returns tuple(sep by ,) of valus and vectors 
print(vals)
print(vecs)

print()
# Singular Value Decomposition 
u,s,vt=la.svd(a) # Unitary array(s) ,Vector(s) with the singular values , unitary arrays 
print(u)
print(s)
print(vt)

print()
      