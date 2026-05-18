

import numpy as np

array = np.arange(1_000_000)
print (array)

pyArray = list(range(1_000_000))
newArray = array * 2 #performing arithmetic operation on array
print(newArray)
newPyArray = [n * 2 for n in pyArray]
