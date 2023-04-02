
## PIAIC Q2 Python Assignment

There is a tale with daily weather data over the last 6 months of 2020, including the maximum, minimum, and average temperatures.
Write a query that gives month, monthly maximum, monthly minimum, mnthly average temperatures for the six months.

```bash
import numpy as np
np.arange(10).reshape(2,5)
```



## Tuple
```bash
arr1 = np.arange(10, dtype = 'int32').reshape(2,5)
arr2 = np.ones(10, dtype = 'int32').reshape(2,5)
np.vstack((arr1, arr2))
```

## 1D Array
```bash
arr1 = np.array([[0,1,2,3,4], [5,6,7,8,9]])
arr1 = np.ravel(arr1)
arr1
```


## High Dimension to 1D Array
```bash
higher_to_lower = np.arange(15).reshape(3,5)
higher_to_lower.ravel()
```
## Create 5x5 an array and find the square of an array?
```bash
five_by_five = np.random.randint(1,10, (5,5))
print(five_by_five)
print('\nSQUARE')
np.square(five_by_five)
```

