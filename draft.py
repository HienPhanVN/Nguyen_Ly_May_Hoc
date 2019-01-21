w, h = 3, 3
Matrix = [[0 for x in range(w)] for y in range(h)]
for x in range(3):
    for y in range(3):
        Matrix[x][y] = input('nhap phan tu o vi tri ['+str(x)+']['+str(y)+']')

for x in range(3):
    for y in range(3):
        print Matrix[x][y],
    print ""
