# Python basic (Part -I) [150 exercises with solution]
# website: https://www.w3resource.com/python-exercises/python-basic-exercises.php

# import
import sys
from datetime import datetime
import math

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

# 11. 
