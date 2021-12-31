# 50+ Basic Python Code Examples
# https://blog.devgenius.io/50-basic-python-code-examples-e1a261c006f5

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
