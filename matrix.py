r = int(input())
c = int(input())
r1 = int(input())
c1 = int(input())
mat = []
mat1 = []
u=0
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    mat.append(a)
for i in range(r1):
    b = []
    for j in range(c1):
        b.append(int(input()))
    mat1.append(b)

for i in range(r):
    c2 = []
    for j in range(c1):
        c2.append(0)
    r.append(c2)

for i in range(len(mat)):
    for j in range(len(mat1[0])):
        for k in range(len(mat1)):
             r[i][j] += mat[i][k] * mat1[k][j]
    print()
for h in r:
   print(h)





