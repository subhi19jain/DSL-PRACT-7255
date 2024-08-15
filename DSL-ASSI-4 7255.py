#ASSIGGNMENT 4 SEARCH ALGORITHMS
def linear_search(student,k):
    linear_count=0
    for x in range (0,len(student)):
        linear_count+=1
        if(student[x]==k):
            print("Linear Count is", linear_count)
            return ("%d is present at %d"%(k,x+1))
    print("Linear Count is", linear_count)
    return ("The Student was absent")

def binary_search(student,k):
    binary_count=0
    start=0
    end=len(student)-1
    while(start<=end):
        binary_count+=1
        mid=(start+end)//2
        if(stu[mid]==k):
            print("Binary Count is", binary_count)
            return ("%d is present at %d"%(k,mid+1))
        elif(student[mid]>k):
            end=mid-1
        elif(student[mid]<k):
            start=mid+1
    print("Binary Count is", binary_count)
    return ("The Student was absent")
        
def sentinel_search(student,k):
    student.append(k)
    i=0
    while(student[i]!=k):
        i+=1
    if(i==len(student)-1):
        return("Not found")
    else:
        return ("%d is present at %d"%(k,i+1))


def fibonacci_search(arr, k, m): 
     
	fib2 = 0
	fib1 = 1 
	fibM = fib2 + fib1 
     
	while (fibM < m): 
		fib2 = fib1 
		fib1 = fibM 
		fibM = fib2 + fib1 
          
	offset = -1

	while (fibM > 1):  
		i = min(offset+fib2, m-1) 
		if (arr[i] < x): 
			fibM = fib1 
			fib1 = fib2 
			fib2 = fibM - fib1 
			offset = i 

		elif (arr[i] > x): 
			fibM = fib2 
			fib1 = fib1 - fib2 
			fib2 = fibM - fib1 

		else: 
			return ("%d is present at %d"%(k,i+1))
          
	if(fib1 and arr[m-1] == x): 
		return ("%d is present at %d"%(k,m))

	return ("Not found")


student=[]
m=int(input("enter the no of students who attended training program : "))
for i in range(0,m) :
   # elements=int(input("roll no%d:"5(i+1) ))
    elements=int(input("Enter the roll no. of student %d: "%(i+1) ))
    list.append(elements)
print(student)
#let the roll no student for whom the search is done be key
key=int(input("Enter the roll number of student to search:"))



    print("  ")
    print(linear_search(students,k))
    print("  ")
    print(binary_search(students,k))
    print("  ")
    print(sentinel_search(students,k))
    print("  ")
    print(fibonacci_search(students,k,m))
    print(" ")
