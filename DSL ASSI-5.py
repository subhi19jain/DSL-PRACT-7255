#assi-5

#linear search 
def linear_search(list,n,key):
    for i in range(0,n):
        if(list[i]==key):
            return i
    return -1

#binary search
def binary_search(list, x):
	low = 0
	high = len(list) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# If x is greater, ignore left half
		if list[mid] < x:
			low = mid + 1

		# If x is smaller, ignore right half
		elif list[mid] > x:
			high = mid - 1

		# means x is present at mid
		else:
			return mid

	# If we reach here, then the element was not present
	return -1




list=[]
m=int(input("enter the no of students who attended training program : "))
for i in range(0,m) :
   # elements=int(input("roll no%d:"5(i+1) ))
    elements=int(input("Enter the roll no. of student %d: "%(i+1) ))
    list.append(elements)
print(list)
#let the roll no student for whom the search is done be key
key=6

n=len(list)
res=linear_search(list,n,key)
if(res==-1):
    print("not attended")
else:
    print("attended " ,res)    



#binary search 
list = [  ]
m=int(input("enter the no of students who attended training program : "))
for i in range(0,m) :
   # elements=int(input("roll no%d:"5(i+1) ))
    elements=int(input("Enter the roll no. of student %d: "%(i+1) ))
    list.append(elements)
print(list)
x = 10

# Function call
result = binary_search(list, x)

if (result== -1):
	print("The student was not present")
	
else:
	print("The student was present ", str(result)) 

        

               

