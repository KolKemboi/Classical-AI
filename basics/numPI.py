import numpy as np

print(np.__version__)

# arrays in numpi
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

array2D = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
print(array2D)
print(array2D.shape)

array3D = np.array([[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
                   [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]])
print(array3D)
print(array3D.shape)

# accessing values
print(arr[1])
print(array2D[1, 3])
print(array3D[1, 1, 3])

# array slicing
print(arr[1:2])
print(array2D[1, 1:3])
print(array3D[1, 1, 1:4])

# copy and view
copied = arr.copy()
arr[2] = 10
print(arr)
print(copied)  # copy creates a whole new array

viewed = arr.view()
arr[2] = 3
print(arr)
print(viewed)  # view "points to the same array"

print(copied.base)  # returns None as it owns its own data
print(viewed.base)  # returns the value of the pointed
