# 50+ Basic Python Code Examples
# https://blog.devgenius.io/50-basic-python-code-examples-e1a261c006f5

# import
import math

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

# 20: prime
def is_prime(num):
    if num == 1 or num == 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

# 1. How to print "Hello World" on Python?
print_color('H', 'E', "Q1")
print("Hello World")

# 2. How to print "Hello + Username" with the user's name on Python?
print_color('H', 'E', "Q2")
# username = input("What is your username?")
username = "seanzou"
print("Hello", username)

# 3. How to add 2 numbers entered on Python?
print_color('H', 'E', "Q3")
num1 = 1
num2 = 2
print(num1, " + ", num2, " = ", num1 + num2)

# 4. How to find the average of 2 Entered Numbers on Python?
print_color('H', 'E', "Q4")
print("Average of ", num1, " and ", num2, " is ", (num1+num2)/2)

# 5. How to calcualte the Entered Visa and Final Grade Average on Python?
print_color('H', 'E', "Q5")
visa_grade  = 94
final_grade = 95
print("0.3 * visa grade + 0.7 * final grade = ", 0.3*visa_grade+0.7*final_grade)

# 6. How to find the Avaerage of 3 Written Grades entered on Python?
print_color('H', 'E', "Q6")
grade1 = 95
grade2 = 89
grade3 = 93
print("Average of grade 1, 2 and 3 is ", (grade1+grade2+grade3)/3)

# 7. How to show the Class Pass Status (PASSED - FAILED) of the student whose Written Average has been entered on Python?
print_color('H', 'E', "Q7")
stu_dict = {'coco':99, 'kiki':80, 'nono':59}
for stu, grade in stu_dict.items():
    if grade >= 60:
        print(stu, "is PASSED")
    elif grade < 60:
        print(stu, "is FAILED")

# 8. How to find out if the entered number is odd or even on Python?
print_color('H', 'E', "Q8")
for num in range(1,10):
    print(num, 'is', end=' ')
    if(num % 2 != 0):
        print('Odd')
    else:
        print('Even')

# 9. How to find out if the entered number is Positive, Negative, or 0 on Python?
print_color('H', 'E', 'Q9')
for num in range(-5,6):
    print(num, 'is', end=' ')
    if(num < 0):
        print('Negative')
    elif(num == 0):
        print('Zero')
    elif(num > 0):
        print('Positive')

# 10. How to calcualte body mass index on Python? BMI
print_color('H', 'E', 'Q10')
bmi_dict = {'coco':(60,1.70), 'kiki':(35, 1.80), 'kuku':(100,1.65)}
for name, values in bmi_dict.items():
    bmi = values[0] / (values[1]*values[1])
    print(name, 'is', end=' ')
    if(bmi < 18.5):
        print('Underweight')
    elif(bmi >= 18.5 and bmi < 25):
        print('Normal Range')
    elif(bmi >= 25 and bmi < 30):
        print('Overweight')
    elif(bmi >= 30):
        print('Obese')

# 11. How to show if the person whose age is entered can get a driver's license on Python?
print_color('H', 'E', 'Q11')
driver_license_dict = {'coco':16, 'kiki':18, 'kuku':22}
for name, age in driver_license_dict.items():
    print(name, 'is', end=' ')
    if age >= 18:
        print('allowed to get a driver\'s license')
    elif age < 18:
        print('not allowed to get a driver\'s license')

# 12. How to List Numbers 1-100 on the Screen on Python?
print_color('H', 'E', 'Q12')
for i in range(1,101):
    print(i, end=', ')
print('')

# 13. How to List Even Numbers 1-100 on Python?
print_color('H', 'E', 'Q13')
for i in range(1,101):
    if i % 2 == 0:
        print(i, end=', ')
print('')

# 14. How to List Odd Numbers 1-100 on Python?
print_color('H', 'E', 'Q14')
for i in range(1,101):
    if i % 2 != 0:
        print(i, end=', ')
print('')

# 15. How to find numbers between 1 and 100 that are divided by 3 and 5 on Python?
print_color('H', 'E', 'Q15')
for i in range(1,101):
    if i % 3 == 0 or i % 5 ==0:
        print(i, end=', ')
print('')

# 16. How to list Numbers from 1 to User-Entered Number on Python?
print_color('H', 'E', 'Q16')
input_num = 10
for i in range(1, input_num+1):
    print(i, end=', ')
print('')

# 17. How to find the Area and Perimeter of a Rectangle With its sides on Python?
print_color('H', 'E', 'Q17')
rec_length = 10
rec_width = 5
print('Area of Rectangle: ', rec_length * rec_width)
print('Perimeter of Rectangle: ', (rec_length + rec_width) * 2)

# 18. How to print the letters of the entered text one under the other on Python?
print_color('H', 'E', 'Q18')
input_letter = 'abcdef'
for c in input_letter:
    print(c, end=' ,')
print('')

# 19. How to show the sum of numbers between two numbers the user has entered on Python?
print_color('H', 'E', 'Q19')
num1 = 1
num2 = 10
sum_num = 0
for i in range(num1, num2+1):
    sum_num += i
print('Sum from ', num1, ' and ', num2, ' is ', sum_num)
print('Sum by sum/1 is ', sum(range(num1, num2+1)))

# 20. For example, let's ask the user about their choice of cinema or theater. You have to pay 10 dollars to watch movies and 5 dollars for theater. We thick that students get 50% discount. If the student is discounted; if he is not a student, let's write a document that calcualtes the non=discounted amount and prints it.
print_color('H', 'E', 'Q20')
per_dict = {'coco':('c',1), 'kiki':('c',0), 'kuku':('t',1)}   # 0: not student, 1: student; 'c': cinema, 't': theater
stu_discount = 0.5
c_price = 10.0
t_price = 5.0
for name, values in per_dict.items():
    if values[0] == 'c':
        place = 'cinema'
        if values[1] == 1:
            price = c_price * stu_discount
        elif values[1] == 0:
            price = c_price
    elif values[0] == 't':
        place = 'theater'
        if values[1] == 1:
            price = t_price * stu_discount
        elif values[1] == 0:
            price = t_price
    print('{0} chose to go to {1}, and he/she needs to pay {2}'.format(name, place, price))

# 21. How to find out if the entered number is Prime or Not on Python?
print_color('H', 'E', 'Q21')
for n in range(1,101):
    if(is_prime(n)):
        print('{0} is Prime'.format(n))
    # else:
        # print('{0} is not Prime'.format(n))

# 22. 
