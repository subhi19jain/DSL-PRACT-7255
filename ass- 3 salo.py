def input_matrix(rows,cols):
    matrix=[]
    print(f"Enter the elements of {rows}*{cols} matrix:")
    for i in range(rows):
        row=[]
        for j in range(cols):
            row.append(int(input("Enter the element [%d][%d]:" %(i,j))))
        matrix.append(row)
    return matrix




def diagonal(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    sum=0
    for i in range(min(rows,cols)):
        sum+=matrix[i][i]
    print(sum)           


def triangle(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    for i in range(rows):
        for j in range(i+1,cols):
            if matrix[i][j]!=0:
                return False
    return True    

def add(matrix1,matrix2):
    rows1,cols1=len(matrix1), len(matrix1[0])
    rows2,cols2=len(matrix2), len(matrix2[0])
    if rows1 != rows2 or cols1!=cols2:
        print("ERROR..")
        return
    result=[[0 for _ in range(cols1)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols1):
            result[i][j]=matrix1[i][j]+matrix2[i][j]
    print(result)

def sub(matrix1,matrix2):
    rows1,cols1=len(matrix1), len(matrix1[0])
    rows2,cols2=len(matrix2), len(matrix2[0])
    if rows1 != rows2 or cols1!=cols2:
        print("ERROR..")
        return
    result=[[0 for _ in range(cols1)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols1):
            result[i][j]=matrix1[i][j]-matrix2[i][j]
    print(result)


def multiply(matrix1,matrix2):
    rows1,cols1=len(matrix1), len(matrix1[0])
    rows2,cols2=len(matrix2), len(matrix2[0]) 

    if cols1  != rows2:
        print("ERROR..")
        return
    else:
        result=[[0 for _ in range(cols1)] for _ in range(rows1)]
        for i in range (rows1):
            for j in range(cols2):
                for k in range(cols1):
                    result[i][j]+=matrix1[i][k]*matrix2[k][j]
        print("result")

def transpose(matrix):    
    rows=len(matrix)
    cols=len(matrix[0])
    transposed=[[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            transposed[i][j]=matrix[j][i]

    return transposed         

def saddle(matrix):
    rows=len(matrix)
    cols=len(matrix[0])

    for i in range(rows):
        min_v=matrix[i][0]
        min_index=0
        for j in range(1,cols):
            if matrix[i][j]<min_v:
                min_v=matrix[i][j]
                min_index=j

        is_saddle=True
        for k in range(rows):
            if matrix[k][min_index]>min_v:
                is_saddle=False
                break

        if is_saddle:
            return((i,min_index),(matrix[i][min_index]))
    return None   

def magic(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    if rows!= cols:
       print("Error...")
       return
    else:
      sum_possible=(rows*(rows*rows+1))/2
      sum1=0
      for i in range(rows):
         for j in range(cols):
            sum1=sum1+matrix[i][j]  
      sum2=0      
      for i in range(cols):
         for j in range(rows):
            sum2=sum2+matrix[i][j] 
             

      
             
        
while True:
  print("1. Sum of Diagonal of matrix")
  print("2. Check wether matrix is upper triangular   ")
  print("3. add two given matrix ")
  print("4. subtract two given matrix ") 
  print("5. Multiplication of two given matrices")  
  print("6. Saddle point of two given matrix")
  print("7. Transpose of matrix ")
  print("8. Check matrix forms a magic square")
  print("9. Exit")
               
  option=int(input("Select any one operation:-"))

  if option == 1:
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = input_matrix(rows, cols)
    diagonal(matrix)
  elif option == 2:
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = input_matrix(rows, cols)
    print(f"Is upper triangular: {triangle(matrix)}")
  elif option == 3:
    rows1 = int(input("Enter the number of rows: "))
    cols1 = int(input("Enter the number of columns: "))
    matrix1 = input_matrix(rows1, cols1)
    rows2=int(input("Enter the number of rows2:"))
    cols2=int(input("Enter the number of cols2:"))
    matrix2=input_matrix(rows2,cols2)
    add(matrix1,matrix2)
  elif option == 4:
    rows1 = int(input("Enter the number of rows: "))
    cols1 = int(input("Enter the number of columns: "))
    matrix1 = input_matrix(rows1, cols1)
    rows2=int(input("Enter the number of rows2:"))
    cols2=int(input("Enter the number of cols2:"))
    matrix2=input_matrix(rows2,cols2)
    sub(matrix1,matrix2)  
  elif option == 5:
    rows1 = int(input("Enter the number of rows: "))
    cols1 = int(input("Enter the number of columns: "))
    matrix1 = input_matrix(rows1, cols1)
    rows2=int(input("Enter the number of rows2:"))
    cols2=int(input("Enter the number of cols2:"))
    matrix2=input_matrix(rows2,cols2)
    multiply(matrix1,matrix2)      
  elif option == 6:
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = input_matrix(rows, cols)
    saddle(matrix)
  elif option == 7:
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = input_matrix(rows, cols)
    transpose(matrix)
  elif option==8:
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = input_matrix(rows, cols)
    magic(matrix)
  elif option==9:
      print("Exiting...") 
      break   
  else:
    print("Invalid option.Please try again...")
