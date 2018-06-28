#IP Homework 4
#Surabhi S Nath- 2016271
#Akshat Singh- 2016128



def swapRows(A,row1,row2):
    A[row1],A[row2]=A[row2],A[row1]
    return A

def Row_Transformation(A, x, row1, row2):
    for j in range(0,len(A[0])):
        A[row2][j]=int(A[row2][j]+x*A[row1][j])    
    return A

def MatrixRank(A):
    rows=len(A)
    cols=len(A[0])

    for i in range(0,rows):
        for j in range(0,cols):
            if A[i][j]!=0:
                for k in range(i+1,len(A)):
                    A=Row_Transformation(A,-(A[k][j]/A[i][j]),i,k)
                break

    noofzerorows=0
    for i in range(0,len(A)):
        L=[]
        for j in range(0,len(A[0])):
            L.append(0)
        if A[i]==L:
            noofzerorows+=1
    return(len(A)-noofzerorows)
