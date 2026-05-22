#Using for loops table

x = int(input("Enter number:  "))

for i in range(1,11):
    print(i , "x" ,x ,"=" , i*x)


#Using while loops tables

x = int(input("Enter number:  "))

i = 1
print("\nTable of " , x ," : \n")
while(i < 11):
    print(i , "x" , x, " = " , i*x)
    i = i+1
