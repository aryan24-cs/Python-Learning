#Function: It is a block of code which is used to perform a specific task.
#It's major advantage is : it reduces the code, enhances the performance, it increases re-usability.

#Syntax of function in python:
#def func_name():
    #task to be performed.

#the name of the function can be anything you want, but it should not be any keyword, and it should be related to the task that is being performed by it. 
#First function using python:

def print_my_name(): #function decalaration
    #Code of task that is to be performed
    print("Vaishnavi")
#call the function
print_my_name()

#Syntax of function with arguments:
#def name(arg1, arg2,....n):
    #code to be performed

#function definition with arguments:
def add_two_numbers(a,b):
    print(a+b)

add_two_numbers(5,5)

#Ques 1: WAP which takes name as argument(input from the user), and then prints the name.
def print_name(name):
    print(f"Welcome! {name}")

a = str(input("Enter your name: "))
print_name(a)

#Functions having return in it: Let's Learn it with an example.

def get_Product(num1, num2):
    product = num1 * num2
    return product
print(get_Product(2,3))



# Practice Questions:
# 1. Calculate the factorial of a number given by the user.
def calc_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
n = int(input("Enter the number: "))
print(calc_factorial(n))

# 2. WAP which takes a number as input and returns the table of it.
def table_of_number(n):
    for i in range(1 , 11):
        result = n*i
        print(result)
table_of_number(5)