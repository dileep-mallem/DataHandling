import numpy as np

a=np.array([[1,2,3],
           [4,5,6]])

# Global Aggregations 
print(np.sum(a)) # sum of all elements 
print(np.min(a),np.max(a)) # min max 

print(np.mean(a)) # 3.5
print(np.median(a)) # 3.5 
print(np.var(a),np.std(a)) # 2.9166666666666665 1.707825127659933
print(np.prod(a)) # 720 -> prod of all emensts 
print(np.cumsum(a,axis=0)) # runnig sum (like cummulative) .cumsum(mtx(m),axis,dtype,out)
# [[1 2 3] axis =0 -> col wise 
#  [5 7 9]]
print(np.cumsum(a,axis=1)) # axis =1 row wise 
# [[ 1  3  6]
#  [ 4  9 15]]


# Aggregation Patterns 

# .sum()

prices=np.array([100,250,75,400,150])

# Count how many prices over 150
print(f"prices over 150 : {(prices>150).sum()}")

# cheacking Elements : .any() .all()

scores=np.array([85,92,45,78,99])

# Did anyone fails < 50 
print((scores<50).any()) # True 

# Did everyone Pass 
print((scores>50).all()) # False