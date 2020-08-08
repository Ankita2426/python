a = int(input("enter number"))
b = int(input("enter no."))
matrix = []
print("enter rows:")
for i in range(a):
    t = []
    for j in range(b):
        t.append(int(input()))
    matrix.append(t)
for i in range(a):
    for j in range(b):
        print(matrix[i][j],end=" ")
    print()
    
