r = int(input())
c=int(input())
mat = []
mat1 =[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    mat.append(a)
for i in range(r):
    b=[]
    for j in range(c):
        b.append(int(input()))
    mat1.append(b)

for i in range(r):
    for j in range(c):
        print(mat[i][j] + mat1[i][j],end=" ")
    print()
