#sparse  matrix


def getMatrix():
    n=int(input("Enter the number of rows:"))
    m=int(input("Enter the number of columns:"))
    sparce_matrix=[[n,m,0]]
    for i in range(0,n):
        for j in range (0,m):
            x=int(input("m[%d][%d]:"%(i+1,j+1)))
            if(x!=0):
                temp=[i,j,x]
                sparce_matrix.append(temp)
                sparce_matrix[0][2]+=1
    return sparce_matrix

def sum_sparce(m1,m2):
    if(m1[0][0]==m2[0][0] and m1[0][1]==m2[0][1]):
        m=m1[0][0]
        n=m1[0][1]
        result=[[m,n,0]]
        x1=x2=1
        count=0
    while(x1<len(m1) and x2<len(m2)):
        if(m1[x1][0]==m2[x2][0] and m1[x1][1]==m2[x2][1]):
            m1[x1][2]=m1[x1][2]+m2[x2][2]
            result.append(m1[x1])
            count+=1
            x1+=1
            x2+=1
        elif(m1[x1][0]==m2[x2][0]):
            if m1[x1][1]<m2[x2][1]:
                result.append(m1[x1])
                count+=1
                x1+=1
            else:
                result.append(m2[x2])
                count+=1
                x2+=1
        else:
            if(m1[x1][0]>m2[x2][0]):
                result.append(m2[x2])
                count+=1
                x2+=1
            else:
                result.append(m1[x1])
                count+=1
                x1+=1
    while(x1<len(m1)):
        result.append(m1[x1])
        x1+=1
        count+=1
    while(x2<len(m2)):
        result.append(m2[x2])
        x2+=1
        count+=1
    result[0][2]=count
    return result

def simple_transpose(mat):
    transpose=[[mat[0][1],mat[0][0],mat[0][2]]]
    for i in range (0,mat[0][1]):
        for j in range (1,mat[0][2]+1):
            if(mat[j][1]==i):
                transpose.append([mat[j][1],mat[j][0],mat[j][2]])
    return transpose

def fast_transpose(sparse):
    s2 = [[sparse[0][1],sparse[0][0],sparse[0][2]]] + [0]* sparse[0][2]
    freq = [0] * (sparse[0][1]+1)
    for i in sparse[1:]:
        freq[(i[1])+1] += 1
    freq[0]=1
    for i in range(1,len(freq)-1):
        freq[i] = freq[i-1]+freq[i]
    for i in sparse[1:]:
        s2[freq[i[1]]] = [i[1],i[0],i[2]]
        freq[i[1]]+=1
    for i in s2:
        print(i)


# Addition of sparse matrices
m1=getMatrix()
m2=getMatrix()
print(" ")
print(m1)
print(" ")
print(m2)
print(" ")
print(sum_sparce(m1,m2))

# Simple_transpose of sparse matrix
m1=getMatrix()
print(" ")
print("the matrix is ")
print(m1)
print(" ")
print("simple transpose of matrix is ")
print(simple_transpose(m1))

# Fast_transpose of sparse matrix
m1=getMatrix()
m2=getMatrix()
print(" ")
print(m1)
print(" ")
print(m2)
print(" ")
print("fast transpose of matrix is ")
print(" ")
print(sum_sparce(m1,m2))
fast_transpose(m1)
