import numpy as np 

rng = np.random.default_rng() # rng -> random number generator

print(rng.integers(1,7)) # end(exl)
print(rng.integers(1,101,size=3)) # [55 73 43]
print(rng.integers(low=1,high=101,size=(3,2)))
# [[17 63]
#  [61 80]
#  [ 6 18]]

# If we want Same Results , we shouls a seed 

rng2=np.random.default_rng(seed=1)
print(rng2.integers(low=1,high=101,size=(3,2)))
# [[48 52]
#  [76 96]
#  [ 4 15]] , for seed = 1, this is same for every user 


# Floating Point Numbers 
print(np.random.uniform()) # 0.011092424934208478
print(np.random.uniform(low=-1,high=1)) # -0.9836808192358684
print(np.random.uniform(-1,1,size=(3,2)))
#[[-0.8740869   0.67139993]
# [-0.09419061  0.55272322]
# [-0.8349747   0.54899182]]

# for setting seed , np.random.seed(seed=1)


# For shuffling an array

rng = np.random.default_rng()

array=np.array([1,2,3,4,5])
rng.shuffle(array)

print(array) # [3 1 2 4 5]

fruits=np.array(["apple","orange","coconut","pineapple"])
print(fruits) # ['apple' 'orange' 'coconut' 'pineapple']

fruit=rng.choice(fruits) # selects any one one
print(fruit) # pineapple

f2=rng.choice(fruits,size=3) # select any three , can select same also for another time
print(f2) # ['coconut' 'orange' 'coconut']

f3=rng.choice(fruits,size=(3,2))
print(f3)
# [['orange' 'orange']
#  ['orange' 'pineapple']
#  ['coconut' 'apple']]

emojies=np.array(["🐉️","🐅️","🦄️","🐼️"])
e=rng.choice(emojies,size=(3,3))
print(e)
# [['🐉️' '🐼️' '🐼️']
#  ['🐼️' '🐅️' '🐅️']
#  ['🐼️' '🐼️' '🦄️']]