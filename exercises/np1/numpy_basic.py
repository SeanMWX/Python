# url: https://www.w3resource.com/python-exercises/numpy/index.php

# import packages
import numpy as np

# for coloring Q1, Q2 ... etc.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'                                                           
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_color(pre, post, word):
    if pre == 'H':
        pre = bcolors.WARNING

    if post == 'E':
        post = bcolors.ENDC

    print(pre + word + post)

# 1. Write a NumPy program to get the numpy version and show numpy build configuration.
print_color('H', 'E', 'Q1')
print(np.__version__)
print(np.show_config())

# 2. Write a NumPy program to  get help on the add function.
print_color('H', 'E', 'Q2')
print(np.info(np.add))

# 3. Write a NumPy program to test whether none of the elements of a given array is zero.
print_color('H', 'E', 'Q3')
a = np.array([1,2,3,4])
print('The array %s' % (a.view()), end=' ')
print('does not contain zero.') if np.all(a) else print('contains zero.')
a = np.array([1,0,2,3,4])
print('The array %s' % (a.view()), end=' ')
print('does not contain zero.') if np.all(a) else print('contains zero.')

# 4. Write a NumPy program to test whether any of the elements of a given array is non-zero.
print_color('H', 'E', 'Q4')
l = [np.array([1,2,3,4]), np.array([0,1,2,3,4]), np.array([0,0,0,0])]
for a in l:
    print('The array %s' % (a.view()), end=' ')
    print('contains non-zero.') if np.any(a) else print('does not contain non-zero.')

# 5. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).
print_color('H', 'E', 'Q5')
# np.nan: not a number
# np.inf: positive infinity
# np.NINF: negative infinity
l = [np.array([np.inf]), np.array([np.NINF]), np.array([0,1,2]), np.array([np.nan,1])]
for a in l:
    print('The array %s' % (a.view()), end=' ')
    print('is for finiteness') if np.all(np.isfinite(a)) else print('is not for finiteness')

# 6. Write a NumPy program to test element-wise for positive or negative infinity.
print_color('H', 'E', 'Q6')
a = np.array([np.inf,1,np.NINF,2,3])
print('For array %s, the positive and negetive infinity are:' % (a.view()))
print([i == np.inf or i == np.NINF for i in a])
# np.isinf()

# 7. Write a NumPy program to test element-wise for NaN of a given array.
print_color('H', 'E', 'Q7')
a = np.array([np.nan, 1, 2, 3, np.inf])
print('For array %s, the NaN are:' %  (a.view()))
print([np.isnan(i) for i in a])

# 8. Write a NumPy program to test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not.
print_color('H', 'E' ,'Q8')
a = np.array([1+1j,2,3,5,0,2j])
print('For array %s' % (a.view()))
print('The complex number:', end=' ')
print([np.iscomplex(i) for i in a])
print('The real number:', end=' ')
print(np.isreal(a))
print('The scalar type:', end=' ')
print([np.isscalar(i) for i in a])

# 9. Write a NumPy program to test whether two arrays are element-wise equal within a tolerance.
print_color('H', 'E', 'Q9')
print('for [1.0], [1.000000001]', np.allclose([1.0], [1.000000001]))
print('for [1.0], [1.1]', np.allclose([1.0], [1.1]))
print('for [1.0], [1.00]', np.allclose([1.0], [1.00]))

# 10. Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.
print_color('H', 'E', 'Q10')
a = np.array([1,2,3,4,5])
b = np.array([5,4,3,3,1])
print('for two arrays %s and %s' % (a.view(), b.view()))
print('==', a == b)
print('<', a < b)
print('>', a > b)

# 11. Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
print_color('H', 'E', 'Q11')
a = np.array([1,2,3])
b = np.array([1,2.00000000001,3.0])
print('Comparison equal:')
print(np.equal(a,b))
print('Comparison equal within a tolerance:')
print(np.allclose(a,b))

# 12. Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.
print_color('H', 'E', 'Q12')
a = np.array([1,7,13,105])
print('The array %s' % (a.view()))
print(a.size * a.itemsize)

# 13. Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.
print_color('H', 'E', 'Q13')
print('10 zeros %s' % (np.zeros((10)).view()))
print('10 ones %s' % (np.ones((10)).view()))
print('10 fives %s' % ((np.ones((10)) * 5)).view())

# 14. Write a NumPy program to create an array of the integers from 30 to 70
print_color('H', 'E', 'Q14')
print('from 30 to 70 %s' % (np.arange(30,71).view()))

# 15. Write a NumPy program to create an array of all the even integers from 30 to 70
print_color('H', 'E', 'Q15')
a = np.array([x for x in range(30,71) if x % 2 == 0])
# print('from 30 to 70 but even %s' % (np.array(a).view()))
print('from 30 to 70 but even %s' % (np.arange(30, 70, 2)))

# 16. Write a NumPy program to create a 3x3 identity matrix
print_color('H', 'E', 'Q16')
print('3x3 identity matrix:')
print(np.identity(3))

# 17. Write a NumPy program to generate a random number between 0 and 1
print_color('H', 'E', 'Q17')
print('generate a random number between 0 and 1')
print(np.random.randint(0,1))

# 18. Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution
print_color('H', 'E', 'Q18')
print('15 random numbers from a standard normal distribution')
print(np.random.normal(0,1,(15)))

# 19. Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last
print_color('H', 'E', 'Q19')
a = np.arange(15,56)
print('all values from 15 to 55 except first and last:')
print(a[1:-1])

# 20. Write a NumPy program to create a 3X4 array using and iterate over it.
print_color('H', 'E', 'Q20')
a = np.zeros((3,4))
for x in np.nditer(a):
    print(x, end=', ')
print('')

# 21. Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50
print_color('H', 'E', 'Q21')
arr = []
for i in range(10):
    if i % 2 == 0:
        arr.append(5)
    else:
        arr.append(50)
a = np.array(arr)
a = np.linspace(5,50,10)
print('vector with length of 10 with values evenly distribtued between 5 and 50 is %s' % (a.view()))

# 22. Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15
print_color('H', 'E', 'Q22')
a = np.arange(0,21)
a[9:16] = -1 * a[9:16]
print(a)

# 23. Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10
print_color('H', 'E', 'Q23')
a = np.random.randint(0, 11, (5))
print(a)

# 24. Write a NumPy program to multiply the values of two given vectors
print_color('H', 'E', 'Q24')
a = np.array([1,2,3])
b = np.array([4,5,6])
print('%s mutiplies %s' % (a.view(), b.view()))
print(a * b)

# 25. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21
print_color('H', 'E', 'Q25')
a = np.arange(10,22)
print('before %s' % (a.view()))
a = np.reshape(a, (3,4))
print('after %s' % (a.view()))

# 26. Write a NumPy program to find the number of rows and columns of a given matrix
print_color('H', 'E', 'Q26')
def find_by_row_column(a, r, c):
    return a[r,c]


a = np.array([[1,2,3],[4,5,6]])
r = 1
c = 2
elem = find_by_row_column(a,r,c)
print('The arr %a' % (a.view()))
print('The %dth row and %dth column\'s element is %d:' % (r, c, elem))
print('The shape of arr:', a.shape)

# 27. Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0
print_color('H', 'E', 'Q27')
print(np.identity(3))

# 28. Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0
print_color('H', 'E', 'Q28')
a = np.zeros((10,10))
a[0,:] = 1
a[-1,:] = 1
a[:,0] = 1
a[:,-1] = 1
print(a)
b = np.ones((10,10))
b[1:-1, 1:-1] = 0
print(b)

# 29. Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5
print_color('H', 'E', 'Q29')
a = np.zeros((5,5))
for i in range(5):
    a[i,i] = i+1
print(a)
b = np.diag([1,2,3,4,5])
print(b)

# 30. Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal
print_color('H', 'E', 'Q30')
a = np.zeros((4,4))
for i in range(a.shape[0]):
    for j in range(a[0].shape[0]):
        if (i+j) % 2 == 0:
            a[i,j] = 0
        else:
            a[i,j] = 1
print(a)
# a[1::2]: start from 1, print every 2th element/row/column
