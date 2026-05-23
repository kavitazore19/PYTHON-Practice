List = [10, 20, 30, "Kavita" , True]
List = [-5, -4, -3 ,  -2   , -1]  #Negative Indexes
print(List)
print(type(List[0]))
print(List[1])
print(List[2])
print(List[3])
print(List[4])

#Printing using for loop
print("\n")
for i in List:
    print(i)

#Negative Indexing
print("\n")
print(List[-3])

#First Converting in positive index 5 - 3 = 2
print(List[len(List) - 3])

#To find any element is in list then

#Method 1

if "Kavita" in List:
    print("Yes")
else:
    print("No")
    

#Method 2

ele = int(input("Enter element to search :  "))
for i in range(len(List)):
      if(List[i] == ele):
       print("Element present at index : " , i)
       break
else:
    print("Element is not present.")



# "in" keyword 
if "vi" in "kavita":
    print("Yes")
else:
    "No"

#To print whole list

print(List[:])
print(List[0:])
print(List[:len(List)])
print(List[-5:5])
print(List[len(List) - 5 : 5])


#Jump Index
#print(marks[start, end , jumpIndex])
#first do slicing for simplicity

marks = [10,20,3,5,5,1,5,5,89,6,100,2,3,841,56]
print(marks[0 : 10])
print()
print(marks[0 : 10 :  3])



#List Comprehension
 
lst = [i for i in range(10)]
print(lst)

lst = [i*i for i in range(10) if i%2 == 0]
print(lst)
