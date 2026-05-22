     #Write a function to find Geometric Mean

#Funtion 1

def CalculateGMean(a, b):
    mean = (a * b) / (a + b)
    print(mean)


#Funtion 2

def FindMax(a , b):

    if(a > b):
        print("First number is greater")
    else:
        print("Second number is greater")


#Pass keyword -> Just telling that i am writing this programme after some time just do further execution

def FindMin(a ,b):
    pass



#Taking Input from user

x = int(input("Enter first number:  "))
y = int(input("Enter Second number:  "))

CalculateGMean(x, y)
FindMax(x ,y)
