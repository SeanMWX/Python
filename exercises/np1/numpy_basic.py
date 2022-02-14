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
