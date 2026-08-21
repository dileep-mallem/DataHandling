
# Sum of squares	     sum(x**2 for x in a)	np.sum(a**2)
# Element-wise multiply	 [a[i]*b[i] for i in range(n)]	a * b
# Filter positives	     [x for x in a if x > 0]	a[a > 0]
# Clip to range	         [max(0,min(10,x)) for x in a]	np.clip(a, 0, 10)
# Running cumulative	 Manual accumulator loop	np.cumsum(a)
# Pairwise distances	 Nested loops O(N²)	LA.norm(X[:,None]-X[None,:],axis=-1)

# When can't you vectorize? 
# Operations where each step depends on the result of the previous step (e.g. certain recurrences) can't be trivially vectorized.
# But 90% of data processing and numerical algorithms can

