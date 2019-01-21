# Cau 1
    A = [2,5,3,6,7,8]
# Cau 2
    B =[]
    for i in range(200):
        B.insert(i,i+1)
        print(B[i])
#Cau 3
    import numpy as np
    B = np.linspace(2,1000,500)
#Cau 4
    A5 = []
    count = 0
    for i in A:
        A5.insert(count,i+5)
        count += 1
#Cau 5
    B3 = []
    count = 0
    for i in B:
        B3.insert(count,i*3)
        count += 1
#Cau 6
    A.sort(reverse=False)
#Cau 7
    Dict = {'Name':'Phan Vo Dinh Hien','Age':22,'Course':'Nguyen Ly May Hoc'}
#Cau 8
    Dict['Course'] = 'Tri Tue Nhan Tao'
#Cau 9
    ten = raw_input("Nhap ten vao : ")
    print("hello "+ten)
#Cau 10
    import numpy as np
    a = input("Nhap a : ")
    b = input("Nhap b : ")
    c = input("Nhap c : ")
    delta = b*b - 4*a*c
    if(delta > 0):
        delta_calculated = np.sqrt(delta)
        x1 = (-b + delta_calculated)/2*a
        x2 = (-b - delta_calculated)/2*a
        print("x1 "+str(x1))
        print("x2 "+str(x2))
    else:
        print("Phuong Trinh Vo Nghiem")
#Cau 11
    array = []
    a = input("Nhap a : ")
    array.insert(0,a)
    b = input("Nhap b : ")
    array.insert(1,b)
    c = input("Nhap c : ")
    array.insert(2,c)
    array.sort(reverse=True)
    print(array[0])
#Cau 12
    w, h = 3, 3
    Matrix = [[0 for x in range(w)] for y in range(h)]
    for x in range(3):
        for y in range(3):
            Matrix[x][y] = input('nhap phan tu o vi tri ['+str(x)+']['+str(y)+']')

    for x in range(3):
        for y in range(3):
            print Matrix[x][y],
        print ""
#Cau 13
    #Cau 12
        w, h = 3, 3
        Matrix = [[0 for x in range(w)] for y in range(h)]
        for x in range(3):
            for y in range(3):
                Matrix[x][y] = input('nhap phan tu o vi tri ['+str(x)+']['+str(y)+']')

        for x in range(3):
            for y in range(3):
                print Matrix[x][y],
            print ""
