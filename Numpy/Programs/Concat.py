import numpy as np

x= np.array([(1,2,3),(3,4,5)])
y= np.array([(1,2,3),(3,4,5)])

print(np.vstack((x,y)))
print(np.hstack((x,y)))

# Below is the Output : 

[[1 2 3] [3 4 5] [1 2 3] [3 4 5]]
[[1 2 3 1 2 3] [3 4 5 3 4 5]]
