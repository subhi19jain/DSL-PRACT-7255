def upper_triangular(matrix):
    for x in range(1,len(matrix)):
        for y in range(0,x):
            if(matrix[x][y]!=0):
                return False
    return True

def sum_diagonal(matrix):
    sum =0
    if len(matrix)!=len(matrix[0]):
        return "Not possible"
    for x in range(0,len(matrix)):
        sum+=matrix[x][x]
    return sum

def transpose(matrix):
    matrix2=[]
    a=len(matrix)
    b=len(matrix[0])
    for x in range(b):
        l=[]
        for y in range (a):
            l.append(0)
        matrix2.append(l)
    
    for x in range(b):
        for y in range (a):
            matrix2[x][y]=matrix[y][x]
    return matrix2

def add(matrix1,matrix2):
    if (len(matrix1)!=len(matrix2) or len(matrix1[0])!=len(matrix2[0])):
        return "Not possible"
    matrix3=[]
    a=len(matrix1)
    b=len(matrix1[0])
    for x in range(a):
        l=[]
        for y in range (b):
            l.append(0)
        matrix3.append(l)
    
    for x in range(0,len(matrix1)):
        for y in range (0,len(matrix1[0])):
            matrix3[x][y]=matrix1[x][y]+matrix2[x][y]
    return matrix3

def subtract(matrix1,matrix2):
    if (len(matrix1)!=len(matrix2) or len(matrix1[0])!=len(matrix2[0])):
        return "Not possible"
    matrix3=[]
    a=len(matrix1)
    b=len(matrix1[0])
    for x in range(a):
        l=[]
        for y in range (b):
            l.append(0)
        matrix3.append(l)
    for x in range(0,len(matrix1)):
        for y in range (0,len(matrix1[0])):
            matrix3[x][y]=matrix1[x][y]-matrix2[x][y]
    return matrix3

def multiply(matrix1,matrix2):
    res=list()
    for x in range(0,len(matrix1)):
        a=[]
        for y in range (0,len(matrix2[0])):
            a.append(0)
        res.append(a)

    for x in range(0,len(matrix1)):
        for y in range (0,len(matrix2[0])):
            for z in range (0,len(mat2)):
                res[x][y]+=matrix1[x][z]*matrix2[z][y]
    
    return res

def saddle(matrix):
    matrix2=transpose(matrix)
    for x in range(0,len(matrix)):
        minimum=min(matrix[x])
        i=matrix[x].index(minimum)
        maximum=max(matrix2[i])
        if(maximum==minimum):
            return((x+1,i+1))
    return "does not exist"

def saddle_one(matrix):
    for x in range(0,len(matrix)):
        minimum=min(matrix[x])
        i=mat[x].index(minimum)
        l=list()
        for y in range (0,len(matrix[0])):
            l.append(matrix[y][i])
        maximum=max(l)
        if (maximum==minimum):
            return ((x+1,i+1))

def get_Matrix():
    n=int(input("Enter no. of rows:"))
    m=int(input("Enter no. of column:"))
    Matrix=[]
    for i in range(0,n):
        x=[]
        for j in range (0,m):
            x.append(int(input("m[%d][%d]:"%(i+1,j+1))))
        Matrix.append(x)
    return Matrix

# print("Matrix 1:")
# matrix1=get_matrix()
# print("Matrix 2:")
# matrix2=get_matrix()
# print("If given matrix is upper triangular or not?")
# print("Matrix 1:",check_triangular(matrix1))
# print("Matrix 2:",check_triangular(matrix2))
# print(" ")
# print("Sum of diagonal elements:")
# print("Matrix 1:",sum_diagonal(matrix1))
# print("Matrix 2:",sum_diagonal(matrix2))
# print(" ")
# print("Transpose of matrix:")
# print("Matrix 1:",transpose(matrix1))
# print("Matrix 2:",transpose(matrix2))
# print(" ")
# print ("Sum of matrix: ",add(matrix1,matrix2))
# print(" ")
# print ("Difference of matrix: ",subtract(matrix1,matrix2))
# print(" ")
# print ("Multiplication of matrix: ",multiply(matrix1,matrix2))
# print(" ")
# print ("Saddle point of matrix:")
# print("Matrix 1:",saddle(matrix1))
# print("Matrix 2:",saddle(matrix2))






print ("Select any of the following operations:")
print("Operation 1: Check whether given matrix is upper triangular or not?")
print("Operation 2: Compute summation of diagonal elements")
print("Operation 3: Computr transpose of matrix")
print ("Operation 4: Add matrix")
print ("Operation 5: Subrtact matrix" )
print ("Operation 6: Multipy matrix" )
print ("Operation 7: Find saddle point")
c=int(input("Enter option number:"))
if(c==1):
    a_Matrix=get_Matrix()
    check=upper_triangular(a_Matrix)
    if(check):
        print("Yes")
    else: 
        print("No")
elif(c==2):
    a_Matrix=get_Matrix()
    print(sum_diagonal(a_Matrix))
elif(c==3):
    a_Matrix=get_Matrix()
    print(transpose(a_matrix))
elif(c==4):
    a_Matrix=get_Matrix()
    b_Matrix=get_Matrix()
    print(add(a_Matrix,b_Matrix))
elif(c==5):
    a_Matrix=get_Matrix()
    b_Matrix=get_Matrix()
    print(subtract(a_Matrix,b_Matrix))
elif(c==6):
    a_Matrix=get_Matrix()
    b_Matrix=get_Matrix()
    print(multiply(a_Matrix,b_Matrix))
elif(c==7):
    a_Matrix=get_Matrix()
    print(saddle(a_Matrix))
