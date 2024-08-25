#assignment - 4 - serching algorithms

# linear search
def lin_search(arr,n,key):
    operations=0  
    for i in range(n):
        operations+=1
        if arr[i]==key:
           return i, operations
    print("Value not found...")  
    return operations  
           

#binary search
def bin_search(arr,n,key):
    f,l=0,n-1
    value=0
    while f<=l:
        mid=(f+l)//2
        value=value+1
        if arr[mid]==key :
           mid=mid+1
           return mid,value
        elif arr[mid]<key:
          f=mid+1
        else:
          l=mid-1  
        
    print("Value not found...")  
    return -1, value   

#sentinal search 
def sentinal_search(arr,n,key):
   arr.append(key)
   i=0
   while arr[i]!= key:
      i+=1
   if i<n:
      return i+1
   else:
      return -1

#fibonacci search      
def fibonacci_search(arr,n,key):
   n=len(arr)
   fib2=0
   fib1=1
   fib=fib2+fib1
   while fib<n:
      fib2=fib1
      fib1=fib
      fib=fib1+fib2
   number=0
   i=0 
   offset=-1
   while fib>1 :
      i=min(offset+fib2,n-1)
      if key<arr[i]:
         fib=fib2
         fib1=fib1-fib2
         fib2=fib-fib1
         number+=1
      elif key>arr[i] :
         fib=fib1
         fib1=fib2
         fib2=fib-fib1
         offset=i 
         number+=1
      else:
         return i,number
      
   return False,number  
   
#input array 
n=int(input("Enter number of value in array: "))
arr=[ 101, 109, 118, 127, 136, 145, 154, 163, 172, 181,
190, 199, 208, 217, 226, 235, 244, 253, 262, 271,
280, 289, 298, 307, 316, 325, 334, 343, 352, 361,
370, 379, 388, 397, 406, 415, 424, 433, 442, 451,
460, 469, 478, 487, 496, 505, 514, 523, 532, 541,
550, 559, 568, 577, 586, 595, 604, 613, 622, 631,
640, 649, 658, 667, 676, 685, 694, 703, 712, 721,
730, 739, 748, 757, 766, 775, 784, 793, 802, 811,
820, 829, 838, 847, 856, 865, 874, 883, 892, 901,
910, 919, 928, 937, 946, 955, 964, 973, 982, 991]




while True:
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Sentinal Search")
    print("4. Fibonacci Search")
    print("5. Exit")
    
    key=int(input("Enter the number to be searched : "))

    option=int(input("Enter the operation option  from the following ( 1/2/3/4/5) : "))    
    if option==1:
      print(lin_search(arr,n,key))
    elif option==2:
      print(bin_search(arr,n,key))   
    elif option==3:
      print(sentinal_search(arr,n,key))
    elif option==4:
      print(fibonacci_search(arr,n,key))   
    else:
      print("Exit")
      break
