
# Ques 1
simplicity and lightweight
accessibility
seamless integration with python
educational purposes

# Ques 2
fixed data type
memory overhead
mutable
single dimensional indexing


# Ques 3
array package is a part standard library provides basic array data structure,
on the other hand numpy is external package made for computing.

NumPy provides a comprehensive collection of mathematical functions and operations 
for working with arrays. while array offers simpler array object with limited functionality 
compared to NumPy.

numpy delivers high performance and array ahs low performance.


# Ques 4
numpy.empty:
The empty function creates a new array without initializing its elements to any specific values

numpy.ones:
The ones function creates a new array filled with ones

numpy.zeros:
The zeros function creates a new array filled with zeros.



# Ques 5
In the numpy.fromfunction function, the callable argument is a function or a callable object 
that defines the relationship between the indices of the array and the values of its elements.




# Ques 6
When a NumPy array is combined with a single-value operand (a scalar) through 
addition, the scaler value is told to match the shape of the array. 
The result is a new array with the same shape as the original array.

import numpy as np

A = np.array([[6, 9], [8, 16]])
n = 2

result = A + n
print(result)



# Ques 7
No, array-to-scalar operations cannot use combined operation-assign operators 
such as += or *=. outcome will be TypeError


# Ques 8
In NumPy, you can create arrays with fixed-length strings using the numpy.string_
If you allocate a longer string to one of these arrays, the behavior depends on 
the string whether it is truncated or raises an error. 


# Ques 9
It will simply add or multiply element to element at same position.

conditions:
shape compatability
broadcasting
data type compatability



# Ques 10
The best way to use a Boolean array to mask another array is by Using 
masked_where of numpy package

# Ques 11
1. Numpy package: it is powerful method of python and it provides effiecient way  
to calculate standard devaition.
import numpy as np
data = np.array([1, 2, 3, 4, 5])
std = np.std(data)

2.statistics method:
import statistics
data = [1, 2, 3, 4, 5]
std = statistics.stdev(data)

3.python calculator:
data = [1, 2, 3, 4, 5]
mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)
std = variance ** 0.5


# Ques 12
it will have same dimensionality as input array.