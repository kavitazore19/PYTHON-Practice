#Break

n = int(input("Enter number:  "))
for i in range(1,12):
    print(n ," x " , i , " = " , n*i )
    if( i == 10):
        break

print("Exit the loop when i becomes 10")



#Continue

a = int(input("Enter number:  "))
for i in range(1,a):
    if(i % 2 == 0):
        continue
    print(i)

print("In this we are skip the even numbers")
