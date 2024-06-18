#importing numpy in our code
import numpy as np 

a= np.array([1,2,3,4,5])
print(type(a))
print(a)
b= np.array((1,4,6,33,5,23))
print(type(b))
print(b)

a = np.array([[1,2,3,4],[2,5,7,9],[2,0,9,7]])
#tryimg to access 2 from third list
print(a[2,0])
#trying to know the dimension of the numpy array
print(a.ndim)


b= np.array([[[1,2,3]],[[7,8,5]],[[8,9,0]]])
print(b.ndim)
#accessing second element of the second list 
print(b[1,0,1])


