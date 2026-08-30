import numpy as np 

a=np.array([10,20,30,40,50])

# Fancy Indexing - index with array od Indeices 
idx=[1,2,4]
print(a[idx]) # [20 30 50]

# 2-D Fancy Indexing 
m=np.array([[1,2],[3,4],[5,6]])

rows=[0,2];cols=[1,0]
print(m[rows,cols]) # [ 2 5] -> m[0,1] and m[2,0]

# Extracting Borders

p=np.arange(1,26).reshape(5,5)
# 1.Using Explicit Fancy Indexing 
# 2.print Expicit;y Top , bootm roes and left and ritht cols 

#**** 3. Create coordinate grids                            # ******

rows, cols = np.indices((5, 5))
mask = (rows == 0) | (rows == 4) | (cols == 0) | (cols == 4)

# Apply fancy indexing via boolean mask
border_elements = p[mask]
print(border_elements)

# Boolean Indexing 
a=np.array([3,-1,4,-2,7])
print(a[a>0]) # [ 3 4 5]
a[a<0]=0 # set -ve as zero
print(a) # [3,0,4,0,7]

#* np.where() -> vectorized if-else  np.where(condition, array , /)
# np.where(onr cond'n) # return new NumPy array of  indecies of Condition True
# np.where(condition , x,y) condition true x , y if Flase 
# The np.where() function does not modify data in place. 
# It acts as a search tool or a filter
a=np.array([1,-2,3,-4])
result=np.where(a>0,a,0) # ReLU: keep positives, zero out negatives
print(f"a : {a} result :{result}") # Here A doent Cahnge 

n=np.arange(10) # [0 1 2 3 4 5 6 7 8 9]
# from 5 all Elemets Should be Squared 
result=np.where(n<5,n,n**2) # [ 0  1  2  3  4 25 36 49 64 81]
print(result)

# np.where with indices only (no replacement)
print(np.where(a>0))  # (array([0, 2]),)  — indices of True elements

#****** We should Square of elemts <5 and Cube >5 and 5 remain 

#1. Using Nested where()
x=np.arange(10)
print(np.where(x<5,x**2,np.where(x>5,x**3,x))) # [  0   1   4   9  16   5 216 343 512 729]

# 2. using np.select()

# we need to oue Conditions and Corrsponding Choics
conditions=[x<5,x>5]
choices=[x**2,x**3]
# If no conditions are met (meaning x == 5), it falls back to the default
result=np.select(conditions,choices,default=x)
print(result)
