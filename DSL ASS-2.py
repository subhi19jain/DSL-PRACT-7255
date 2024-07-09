#DSL ASS-2
#INPUT 
# SET A = Students who play cricket
# SET B = Students who play badminton
# SET C = Students who plau football

#INTERSECTION
def P1NP2 (P1,P2):
    N=[]
    for i in P2:
        if (i in P1):
            N.append(i)
    return N

#UNION
def P1UP2 (P1,P2):
    U=[]
    for i in P1:
        U.append(i)
    for i in P2:
        if ( i not in P1):
            U.append(i)
    return U

#DIFFERNCE
def P1minusP2 (P1,P2):
    Diff=[]
    for i in P1:
        if(i not in P2):
            Diff.append(i)
    return Diff

tstudents=int(input("Enter the total no. of students: "))

a = eval(input("Enter Roll no. of students who play cricket: "))
b = eval(input("Enter Roll no. of students who play badminton: "))
c = eval(input("Enter Roll no. of students who play football: "))


#1 List of students who play both cricket and badminton i.e 'A' N 'B'

print("The roll nos. of students who play both cricket and badminton:")
print(P1NP2(a,b))

#2 List of studnts who play either cricket or badminton but not both i.e {A U B}-{A N B}

print("The roll nos. of students who play either cricket or badminton but not both:")
print(P1minusP2(P1UP2(a,b),P1NP2(a,b)))

#3 No of students who play neither cricket nor badminton

print("The number of students who play neither cricekt nor badminton are: ")
print(tstudents-len(P1UP2(a,b)))

#4 No of student who play cricket and football but not badminton

print("The number of students who play cricket and football but not badminton are:")
print(len(P1minusP2(P1NP2(a,c),b)))

#5 No of students who do not play any game

print("The total no of students who do not play any game are:")
print(tstudents-len(P1UP2(a,(P1UP2(b,c)))))

#6 List of studetns who play at least one game

print("The roll nos. of student who play atleast one game:")
print(P1UP2(a,P1UP2(b,c)))

#7 List of students who play all the games

print("The roll nos. of the students who play all the games are:")
print(P1NP2(a,P1NP2(b,c)))
