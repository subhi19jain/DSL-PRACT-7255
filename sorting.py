# ASSIGNMENT 6- SORTING ALGORITHMS 

def bubbleSort(list):
      n= len(list)
      number=0
      for i in range(n):
            check=False
            for j in range (0,n-i-1):
                  if list[j]>list[j+1]:
                        list[j],list[j+1]=list[j+1],list[j]
                        print(list)
                        number+=1
                  check=True
            if check==False:
                  break
      print(number)


def selectionSort(list):
      n=len(list)
      count=0
      for i in range(n):
            min=i
            for j in range(i+1,n):
                  if list[j]<list[min]:
                        min=j
                        count+=1
            list[i],list[min]=list[min],list[i]
            print(list)

      print(count)



m=eval(input("Enter the no. of students in first year : "))
list=[]
list=eval(input("Enter the percentages of students list:  "))


list1=list.copy()
while (True):
      print("Option1: Bubble sort")
      print("Option2: Selection sort")
      print("Option3: Exit")

      option=int(input("Enter one of the following options: "))
      

      if option==1:
            print("list: " , list)
            bubbleSort(list)
            
      elif(option==2) :
            print("list: ",list1)
            selectionSort(list1)

      else:
            print("END")
            break 


     
            # for i in range(0,m) :
#    # elements=int(input("roll no%d:"%(i+1) ))
#     elements=eval(input("Enter the percentages of students  %d: "%(i+1) ))
#     list.append(elements)
# print("unsorted list is : ")    
# print(list)
# size=len(list)
# selectionSort(list,size)
# print("the sorted list after selection sort is : ")
# print(list)
