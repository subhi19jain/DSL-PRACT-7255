#ASSIGNMENT 4 - SEARCH ALGORITHMS 

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Execution time of {func.__name__}: {execution_time:.4f} milliseconds")
        return result
    return wrapper

a=[]


def linearSearch(lst,stu):
    ret=-1
    count=0
    for i in range(len(lst)):
        count+=1
        if lst[i]==stu:
            ret=i
            break
    return ret,count


def binarySearch(lst,s,e,stu,count = 0):
    if s>e:
        return (-1,count)
    else:
        s=s
        e=e
        m=int((s+e)/2)
        if lst[m]==stu:
            return (m,count)
        elif stu>lst[m]:
            return binarySearch(lst,m+1,e,stu,count+1)
        elif stu<lst[m]:
            return binarySearch(lst,s,m-1,stu,count+1)


def binarySearch2(lst,stu):
    s=0
    e=len(lst)-1
    while(s<e):
        m=(s+e)//2
        if lst[m]==ele:
            return m
        elif stu>lst[m]:
            s=m+1
        elif stu<lst[m]:
            e=m-1
    pass

def sentinalSearch(lst,stu):
    lst2 = lst.copy()
    lst2.append(stu)
    i=0
    count = 0
    while lst2[i]!=stu:
        i+=1
        count+=1
    if i<len(lst2)-1:
        return i,count
    else:
        return -1,count
    

def fibonacciSearch(arr,stu):
    count = 0
    offset = 0
    fibm = 1
    fibm1 = 0
    fibm2 = 0
    while fibm < len(arr):
        fibm2 = fibm1
        fibm1 = fibm
        fibm = fibm1 + fibm2
    while fibm > 1:
        i = min(offset + fibm2, len(arr)-1)
        if arr[i] < ele:
            fibm = fibm1
            fibm1 = fibm2
            fibm2 = fibm - fibm1
            offset = i
            count += 1
        elif arr[i] > stu:
            fibm = fibm2
            fibm1 = fibm1 - fibm2
            fibm2 = fibm - fibm1
            count += 1
        elif arr[i] == stu:
            return i,count
    return -1,count


input_str_a = input("Enter no of students : ")
a = input_str_a.split()  
a = sorted([int(num) for num in a])
stu=int(input("Enter the student to be searched : "))

@measure_time
def binaryCheck():
    print()
    print("Using Binary Search")
    ans = binarySearch(a,0,len(a),stu)
    if ans[0]<0:
        print("student not found")
        print("The no of comparisions:",ans[1])
        
    else:
        print("student found at", ans[0])
        print("The no of comparisions:",ans[1])
@measure_time
def linearCheck():
    print()
    print()
    print("Using linear search")
    ans = linearSearch(a,stu)
    if ans[0]<0:
        print("student not found")
        print("The no of comparisions:",ans[1])
    else:
        print(f"student found at", ans[0])
        print("The no of comparisions:",ans[1])
@measure_time
def sentinalCheck():
    print()
    print()
    print("Using sentinal search")
    ans = sentinalSearch(a,stu)
    if ans[0]<0:
        print("student not found")
        print("The no of comparisions:",ans[1])
    else:
        print(f"student found at", ans[0])
        print("The no of comparisions:",ans[1])
@measure_time
def fibonacciCheck():
    print()
    print()
    print("Using fibonacci search")
    ans = fibonacciSearch(a,stu)
    if ans[0]<0:
        print("student not found")
        print("The no of comparisions:",ans[1])
    else:
        print(f"student found at", ans[0])
        print("The no of comparisions:",ans[1])


linearCheck()
sentinalCheck()
binaryCheck()
fibonacciCheck()
