# ASSIGNMENT NO-1 :  Marks of N students in FDS
#1 average score of class
def average(a):
    avgi=0
    for i in range (numstudent):
        if a[i] >=0:
            avgi=avgi+a[i]
    print("The average marks of students are : ",avgi/numstudent)
    #print(sumi/numstudent)

#2 highest and lowest score of the class
def highlow(list):
    max=0
    min=100
    for i in range (0,numstudent):
        if list[i]<max:
            max=list[i]
        if list[i]>min: #and list[i]>=0:
            min=list[i]
    print("Highest marks is :" ,max)
    print("Lowest marks is :" , min)

#3 Count of absent students
def countabsenties(list):
    count=0
    for i in range (0,numstudent):
        if list[i]==-1 :
            count=count+1
    print("The number of absent students are:" , count)

#4 Percentages-passed & failed considering passing marks are 33
def perpassfail(list):
    numpass=0
    numfail=0
    for i in range (0,numstudent):
        if list[i]>=33:
            numpass=numpass+1
        else:
            numfail=numfail+1
    print("Percentage of passed students is:" , numpass/numstudent*100)
    print("Percentage of failed students is:" , numfail/numstudent*100)

#5 Marks with highest frequency

def highestfreq(marklist):
    frequency_dict = {}
    for x in marklist:
        if x in frequency_dict:
            frequency_dict[x] +=1
        else :
            frequency_dict[x] = 1
    highest_f = max(frequency_dict.values())
    key_list = list(frequency_dict.keys())
    value_list= list(frequency_dict.values())
    print("highest frequency is:")
    for x in range(len(value_list)):
        if(value_list[x]==highest_f):
            print(key_list[x])


numstudent=int(input("Enter the number of students : "))
student_list=list()
for i in range(0,numstudent) :
    marks=int(input("Enter the marks of roll no. %d: "%(i+1) ))
    student_list.append(marks)
average(student_list)
highlow(student_list)
countabsenties(student_list)
perpassfail(student_list)
highestfreq(student_list)




