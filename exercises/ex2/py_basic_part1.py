# Python basic (Part -I) [150 exercises with solution]
# website: https://www.w3resource.com/python-exercises/python-basic-exercises.php

# import
import sys
from datetime import datetime
import math
# 12. calendar
import calendar
# 14
from datetime import date

# for coloring
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

# 1. Write a Python program to print the following string in a specific format (see the output).
print_color('H', 'E', 'Q1')
print('Twinkle, twinkle, little star,')
print('\tHow I wonder what you are!')
print('\t\tUp above the world so high,')
print('\t\tLike a diamond in the sky.')
print('Twinkle, twinkle, little star,')
print('\tHow I wonder what you are')

# 2. Write a Python program to get the Python version you are using.
print_color('H', 'E', 'Q2')
print('Your current python version is {0}.{1}.{2}'.format(sys.version_info[0], sys.version_info[1], sys.version_info[2]))

# 3. Write a Python program to display the current date and time.
print_color('H', 'E', 'Q3')
now = datetime.now()
print('Current data and time:')
print(now.strftime('%y-%m-%d %H:%M:%S'))

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
print_color('H', 'E', 'Q4')
r = 1.1
print('r = {0}\nArea = {1}'.format(r, math.pi*r*r))

# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
print_color('H', 'E', 'Q5')
first_name = 'xinhai'
last_name = 'pigpig'
print('{0} {1}'.format(last_name, first_name))

# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
print_color('H', 'E', 'Q6')
input_nums = '3,5,7,23'
lst = input_nums.split(',')
tple = tuple(lst)
print(lst)
print(tple)

# 7. Write a Python program to accept a filename from the user and print the extension of that.
print_color('H', 'E', 'Q7')
filename = 'abc.java'
print(filename.split('.')[-1])

# 8. Write a Python program to display the first and last colors from the following list.
print_color('H', 'E', 'Q8')
color_list = ["Red","Green","White" ,"Black"]
print('First color: {0}; Last color: {1}'.format(color_list[0], color_list[-1]))

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
print_color('H', 'E', 'Q9')
exam_st_date = (11,12,2014)
def ex_schedule(date):
    return '{0}/{1}/{2}'.format(date[0], date[1], date[2])


print('The examination will start from: {0}'.format(ex_schedule(exam_st_date)))

# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
print_color('H', 'E', 'Q10')
num = 5
print('Expected Result: {0}'.format(num*3+num*10*2+num*100))

# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s)
print_color('H', 'E', 'Q11')
num_list = [-10, -5, 0, 5]
abs_list = []
for num in num_list:
    if num < 0:
        abs_list.append(num * -1)
        continue
    abs_list.append(num)
print('Original: {0}'.format(num_list))
print('Absolute: {0}'.format(abs_list))

# *Calendar
# *12. Write a Python program to print the calendar of a given month and year.
print_color('H', 'E', 'Q12')
y = 2022
m = 1
print(calendar.month(y, m))

# *multi print
# *13. Write a Python program to print the following 'here document'
print_color('H', 'E', 'Q13')
print('''
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
'''
)

# 14. Write a Python program to calculate number of days between two dates.
print_color('H', 'E', 'Q14')
date1 = date(2014,7,2)
date2 = date(2014,7,11)
print('The days difference between {0} and {1} is {2}'.format(date1, date2, (date2-date1).days))

# 15. Write a Python program to get the volume of a sphere with radius 6.
print_color('H', 'E', 'Q15')
r = 6
print('The volume of sphere with radius of {0} is {1}'.format(r, 4/3*math.pi*r**3))

# 16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
print_color('H', 'E', 'Q16')
num_list = [-1, 1, 18, 20]
for num in num_list:
    print('For \'{0}\', the difference is '.format(num), end='')
    if num > 17:
        print((num-17)*2, '[double]')
    else:
        print(abs(17-num))

# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
print_color('H', 'E', 'Q17')
num_list = [100,901,1001,1990,2022,2200]
for num in num_list:
    print('For \'{0}\''.format(num), end=' ')
    if abs(1000-num) <= 100 or abs(2000-num) <= 100:
        print('is within 100 of 1000 or 2000')
    else:
        print('is not wihtin 100 of 1000 or 2000')

# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
print_color('H', 'E', 'Q18')
num_list1 = [1,1,1]
num_list2 = [1,2,1]
num_lists = [num_list1, num_list2]
for lst in num_lists:
    temp = None
    is_same = True
    for num in lst:
        if temp is None:
            temp = num
            continue
        if temp != num:
            is_same = False
            break
    if is_same:
        print('For {0}, the 3 times sum is: {1}'.format(lst, sum(lst)*3))
    else:
        print('For {0}, the sum is: {1}'.format(lst, sum(lst)))

# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
print_color('H', 'E', 'Q19')
str_list = ['Coco is cool', 'Is Kiki is cool', 'Is kuku is cool']
new_str_list = []
for _str in str_list:
    if _str.split(' ')[0] != 'Is':
        _str = 'Is ' + _str
    new_str_list.append(_str)
print('Original: ', str_list)
print('Add \'Is\': ', new_str_list)

# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.
print_color('H', 'E', 'Q20')
n = 5
str1 = 'Hello world!'
for i in range(n):
    print(str1)

# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
print_color('H', 'E', 'Q21')
num_list = [1,2,3,4,5]
for num in num_list:
    print('For {0}, it is '.format(num), end='')
    if num % 2 != 0:
        print('Odd number.')
    elif num % 2 == 0:
        print('Even number.')

# 22. Write a Python program to count the number 4 in a given list.
print_color('H', 'E', 'Q22')
num_list = [1,2,4,5,54,4,4,4,4]
count = 0
for num in num_list:
    if num == 4:
        count += 1
print('The number 4 appears {0} times'.format(count))

# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
print_color('H', 'E', 'Q23')
str_lst = ['a', 'abc']
n = 3
for _str in str_lst:
    if len(_str) < 2:
        for i in range(n):
            print(_str)
    else:
        for i in range(n):
            print(_str[0]+_str[1])

# 24. Write a Python program to test whether a passed letter is a vowel or not.
print_color('H', 'E', 'Q24')
c_list = ['a','b','c','e','o','z']
for c in c_list:
    print('{0}'.format(c), end=' ')
    # best solution: if c in 'aeiou'
    if c in ['a', 'e', 'i', 'o', 'u']:
        print('is Vowel')
    else:
        print('is not Vowel')

# 25. Write a Python program to check whether a specified value is contained in a group of values.
print_color('H', 'E', 'Q25')
num_list = [-1,1,3,5,7]
check_list = [1,3,7]
for num in num_list:
    print('{0} -> {1}:'.format(num, check_list), end=' ')
    if num in check_list:
        print('True')
    else:
        print('False')

# 26. Write a Python program to create a histogram from a given list of integers.
print_color('H', 'E', 'Q26')
num_list = [1,5,7,10]
for num in num_list:
    for i in range(num):
        print('*', end='')
    print('')

# 27. Write a Python program to concatenate all elements in a list into a string and return it.
print_color('H', 'E', 'Q27')
conc_list = [1,'s','coco','2','a','kiki']
conc_str = ''
for elem in conc_list:
    conc_str += str(elem)
print('The concat string is {0}'.format(conc_str))

# 28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
print_color('H', 'E', 'Q28')
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,958,743, 527]
for num in numbers:
    if num == 237:
        print(num, end=',')
        break
    if num % 2 == 0:
        print(num, end=',')
print('')

# 29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
print_color('H', 'E', 'Q29')
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
color_selected = set([])
#for color in color_list_1:
#    if color not in color_list_2:
#        color_selected.add(color)
color_selected = color_list_1.difference(color_list_2)
print(color_selected)

# 30. Write a Python program that will accept the base and height of a triangle and compute the area.
print_color('H', 'E', 'Q30')
base = 3
height = 4
print('Area of triangle: {0}'.format(base*height*1/2))

# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
print_color('H', 'E', 'Q31')
nums_list = [(12,17), (4,6), (336,360)]
def gcd(big, small):
    tmp = big - small
    if tmp == 0:
        return big
    if tmp > small:
        return gcd(tmp, small)
    else:
        return gcd(small, tmp)


for nums in nums_list:
    print('For {0} and {1}, gcd is {2}'.format(nums[0], nums[1], gcd(nums[1],nums[0])))

# 32. Write a Python program to get the least common multiple (LCM) of two positive integers.
print_color('H', 'E', 'Q32')
nums_list = [(12,17), (4,6), (15,17)]
def lcm(big, small):
    return big*small/gcd(big,small)


for nums in nums_list:
    print('FOr {0} and {1}, lcd is {2}'.format(nums[0], nums[1], lcm(nums[1], nums[0])))

# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
print_color('H', 'E', 'Q33')
nums_list = [[1,2,3],[3,4,5],[5,5,6]]
for nums in nums_list:
    print('For list {0}, '.format(nums), end='')
    _sum = 0
    if len(nums) != len(set(nums)):
        _sum = 0
    else:
        for num in nums:
            _sum += num
    print('the sum is {0}'.format(_sum))

# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
print_color('H', 'E', 'Q34')
nums_list = [[1,2], [3,4], [5,6], [5,10]]
for nums in nums_list:
    print('For list {0}, '.format(nums), end='')
    if sum(nums) >= 15 and sum(nums) <= 20:
        print('the sum is {0}'.format(20))
    else:
        print('the sum is {0}'.format(sum(nums)))

# 35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
print_color('H', 'E', 'Q35')
nums_list = [[2,2], [3,4], [5,5], [5,10]]
for nums in nums_list:
    print('For list {0}, '.format(nums), end='')
    if nums[0] == nums[1] or abs(nums[0]-nums[1]) == 5:
        print ('is True')
    else:
        print('is False')

# 36. Write a Python program to add two objects if both objects are an integer type.
print_color('H', 'E', 'Q36')
nums_list = [[2,2], [3.1,4], [5,5.3], [5,10]]
for nums in nums_list:
    print('For list {0}, '.format(nums), end='')
    if isinstance(nums[0],int) and isinstance(nums[1], int):
        print('the sum is {0}'.format(sum(nums)))
    else:
        print('they are not both integer')

# 37. Write a Python program to display your details like name, age, address in three different lines.
print_color('H', 'E', 'Q37')
class Person():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


p1 = Person('CoCo', 20, 'Earth')
print('Name: {0}, Age: {1}, Address: {2}.'.format(p1.name, p1.age, p1.address))

# 38. Write a Python program to solve (x + y) * (x + y). 
print_color('H', 'E', 'Q38')
num_list = [(1,2),(4,3)]
for num in num_list:
    x = num[0]
    y = num[1]
    print('(({0}+{1})^2)={2}'.format(x,y,(x+y)**2))

# 39. 

