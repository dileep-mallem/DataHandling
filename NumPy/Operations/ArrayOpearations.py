import numpy as np 

a=np.array([1,2,3,4])
b=np.array([10,20,30,40])

# Element Wise Arithmetic No Loops Needed (Shapes Should be According to Requirement of Opearion)

print(a+b)
print(b-a)
print(a*b)
print(b//a)
print(a**2)
print(b%10)
print("\nScalar Broadcasting \n")

# Logical AND (&)
print((a>15) & (b<4)) # [False  True  True False]
#logical OR (|)
print((a>15) | (b<4)) # [ True  True  True  True]
print()


# Scalar Broadcasting -> Scalar applied to every Element 
print(a*5)
print(a+10)

# Comaparision -> returns Boolean Array 
print(a>2)
print(a==b//10)

# Dot product and Matrix Multiplication 
print(np.dot(a,b)) # 300  (1*10 + 2*20 + 3*30 + 4*40)
m1=np.array([[1,2],[3,4]])
m2=np.array([[5,6],[7,8]])
print(m1 @ m2) # matrix multiplication (@ operator)

