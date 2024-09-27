def radixsort_with_buckets(arr):
    if not arr:
        return arr
    
    max_num=max(arr)
    pos=1
    while max_num// pos>0:
        buckets=[[] for _ in range(10) ]

        for number in arr:
            digit=(number//pos)%10
            buckets[digit].append(number)


        arr=[]
        for bucket in buckets:
            arr.extend(bucket)
        pos*=10

    return arr


def countSort(arrayy):
    size=len(arrayy)
    output =[0]*size
    count=[0]*(max(arrayy)+1)
    for i in range(0,size):
        count[arrayy[i]]+=1

    for i in range(1,(max(arrayy)+1)):
        count[i]+=count[i-1]
    i=size-1
    while i>=0:
        output[count[arrayy[i]]-1]=arrayy[i]
        count[arrayy[i]]-=1
        i-=1
    for i in range(0,size):
        arrayy[i]=output[i]


def partition(arrayy,low,high):
    pivot=arrayy[high]
    i=low-1
    for j in range(low,high):
        if arrayy[j]<=pivot:
            i=i+1
            (arrayy[i],arrayy[j])=(arrayy[j],arrayy[i])
    (arrayy[i+1],arrayy[high])=(arrayy[high],arrayy[i+1])
    return i+1


def quickSort(arrayy,low,high):
    if low<high:
        pi=partition(arrayy,low,high)
        quickSort(arrayy,low,pi-1)
        quickSort(arrayy,pi+1,high)

n=int(input("Enter number of elements : "))
l=eval(input("Enter the list : "))


# #1
# print("Sorted list: ")
# #starttime1=datetime.now()

# print()
# print("Bucket sort ")
# print(radixsort_with_buckets(l))


# #endtime1=datetime.now()
# #print("\n Time taken : ")

# #2
# print("sorted list : ")

# print()
# print("bucket sort ")
# print(countSort(l))


#3
print("sorted list : ")
print()
print("QUICK SORT")
print(quickSort(l,0,len(l)-1))


