
def Average(a , b):
    print("The average is " ,(a + b) / 2)


x = int(input("Enter first number:  "))
y = int(input("Enter second numbre:  "))

Average (x, y)

#1.Default Arguments

def average(a = 9, b = 1):
    print("The average is : " , (a+b) / 2)

average(b=9)  #a is taking by degault as 9
average(a=3)  # b is taking by default as 1
average(a=1, b=5) #it ignores a = 9, b = 1 and taking 1 and 5

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello ", fname , mname, lname)

name("Amy")


#2. Keyword Arguments

#Dont need to take care of order 

def Gmean(a = 3, b = 9):
    print("Geometric mean : ", (a*b) / (a + b))

Gmean(b = 9, a = 3)


# 3.Required Argumnets

#Here required argument is a you must have to give any value for a
#This causes error

def Sum(b=3):
    print(a + b)

Sum(a,b=9)

# 4.Variable length argument

def Average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

a = Average(7,9,2,5)  #you can pass any total numbers you want to pass

print("Average is: " , a)
