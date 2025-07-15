#Default Arguments in python:
#A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument. 
#Example of Default Argument.
def sam(a, b=20):
    print(a+b)
sam(22)

#Keyword Arguments:
# The idea is to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.
#Example:
def print_full_name(firstName, lastName):
    print(firstName)
    print(lastName)

#calling the function:
print_full_name(lastName="Pandey",firstName="Satyam")

#Example 2:
def get_exp(base, exp):
    result= base ** exp
    return result
#calling the function
print(get_exp(exp=10,base=2))

# #Python Function within Functions:
# #A function that is defined inside another function is known as the inner function or nested function. Nested functions can access variables of the enclosing scope. Inner functions are used so that they can be protected from everything happening outside the function.

# #Example:
def func1(name):
    print(name)
    age = 20
    def func2():
        print(age)
    func2() #calling in the func1
func1("Satyam")



#Practice Question of above mentioned topics:
#Ques 1: Write a function to calculate the square of a number?
def get_a_square(n):
    result = n*n
    return result
n = int(input("Enter a number:"))
print(get_a_square(n))

# Ques 2: Create a function to reverse a string?
def reverse_a_string(s):
    result = ""
    for char in s:
        result= char + result
    print(result)
s =  str(input("Enter a string type name :"))
reverse_a_string(s)

#Ques 3: Check a string is a palindrome or not?

def isPalindrome():
    s = str(input("Enter a string: "))
    res = ""
    for char in s:
        res = char + res
    print(res) #To check that the string is reversed or not
    if(s==res):
        print("Yes")
    else:
        print("No")
isPalindrome()
