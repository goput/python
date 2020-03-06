def triangle_topright(long):
    data = ""
    row = 1
    for i in range (row, long+1):
        column = row
        for i in range (1, column):
            data = data + " "
            column = column - 1
        right_side = 0
        for i in range (right_side, ((long+1) - row)):
            data = data + "*"
            right_side = right_side + 1
        data = data + "\n"
        row = row + 1
    print(data)

def triangle_bottomright(long):
    data = ""
    row = long
    for i in range (0, row):
        column = row
        for i in range (0, column):
            data = data + " "
            column = column - 1
        right_side = 0
        for i in range (right_side, (long - (row-1))):
            data = data + "*"
            right_side = right_side + 1
        data = data + "\n"
        row = row - 1
    print(data)

def triangle_topleft(long):
    data = ""
    row = long
    for i in range (0, row):
        column = row
        for i in range (0, column):
            data = data + "*"
            column = column - 1
        data = data + "\n"
        row = row - 1
    print(data)

def triangle_bottomleft(long):
    data = ""
    row = 1
    for i in range (row, long+1):
        column = row
        for i in range(0, column):
            data = data + "*"
            column = column - 1
        data = data + "\n"
        row = row + 1
    print(data)

def isosceles_triangle_reverse(long):
    data = ""
    row = 1
    for i in range (row, long+1):
        column = row
        for i in range (0, column):
            data = data + " "
            column = column - 1
        left_side = 0
        for i in range (left_side-1, (long - row)):
            data = data + "*"
            left_side = left_side + 1
        right_side = left_side
        for i in range (0, right_side-1):
            data = data + "*"
            right_side = right_side - 1
        data = data + "\n"
        row = row + 1
    print(data)

def isosceles_triangle(long):
    data = ""
    row = long
    for i in range (0, row):
        column = row
        for i in range (0, column):
            data = data + " "
            column = column - 1
        left_side = 0
        for i in range (left_side, (long - (row - 1))):
            data = data + "*"
            left_side = left_side + 1
        right_side = 1
        for i in range (right_side, (long - (row-1))):
            data = data + "*"
            right_side = right_side + 1
        data = data + "\n"
        row = row - 1
    print(data)

def diamond_star(long):
    data = ""
    row = long
    for i in range (0, row + 1):
        column = row + 2
        for i in range (1, column):
            data = data + " "
            column = column - 1
        left_side = 0
        for i in range (left_side, (long - row)):
            data = data + "*"
            left_side = left_side + 1
        right_side = 0
        for i in range (right_side, (left_side - 1)):
            data = data + "*"
            right_side = right_side + 1
        data = data + "\n"
        row = row - 1
    row = 1
    for i in range (row, long):
        column = row + 2
        for i in range (1, column):
            data = data + " "
            column = column - 1
        left_side = 0
        for i in range (left_side, (long - row)):
            data = data + "*"
            left_side = left_side + 1
        right_side = left_side
        for i in range (1, right_side):
            data = data + "*"
            right_side = right_side - 1
        data = data + "\n"
        row = row + 1
    print(data)

def hourglass_star(long):
    data = ""
    row = 1
    for i in range (row, long):
        column = row
        for i in range (1, column):
            data = data + " "
            column = column - 1
        left_side = 0
        for i in range (left_side-1, (long - row)):
            data = data + "*"
            left_side = left_side + 1
        right_side = left_side
        for i in range (1, right_side):
            data = data + "*"
            right_side = right_side - 1
        if (row+1 <= long) :
            data = data + "\n"
        row = row + 1

    row = long - 1
    for i in range (0, row + 1):
        column = row
        for i in range (0, column):
            data = data + " "
            column = column - 1
        left_side = 1
        for i in range (left_side, (long - (row - 1))):
            data = data + "*"
            left_side = left_side + 1
        right_side = 0
        for i in range (right_side, (left_side-2)):
            data = data + "*"
            right_side = right_side + 1
        data = data + "\n"
        row = row - 1
    print(data)

def star_shape():
    title = "STAR MENU"
    triangle_menu = ["Triangle Top Right","Triangle Bottom Right","Triangle Top Left", "Triangle Bottom Left", "Isosceles Triangle", "Isosceles Reverse Triangle"]
    extra_menu = ["Diamond", "HourGlass"]
    menu = triangle_menu + extra_menu
    print(10*"=",title,10*"=")
    for i in range(0,len(menu)):
        print(i+1, menu[i])
    choice = int(input("Choice your star menu : "))
    print(50*"=")
    if(choice == 1):
        print(10*"=",menu[choice-1],10*"=")
        long = int(input("How long do you want : "))
        triangle_topright(long)
    elif(choice == 2):
        print(10*"=",menu[choice-1],10*"=")
        long = int(input("How long do you want : "))
        triangle_bottomright(long)
    elif(choice == 3):
        print(10*"=",menu[choice-1],10*"=")
        long = int(input("How long do you want : "))
        triangle_topleft(long)
    elif(choice == 4):
        print(10*"=",menu[choice-1],10*"=")
        long = int(input("How long do you want : "))
        triangle_bottomleft(long)
    elif(choice == 5):
        print(10*"=",menu[choice-1],10*"=")
        long = int(input("How long do you want : "))
        isosceles_triangle(long)
    elif(choice == 6):
        print(10*"=",menu[choice-1],10*"=")
        long = int(input("How long do you want : "))
        isosceles_triangle_reverse(long)
    elif(choice == 7):
        print(10*"=",menu[choice-1],10*"=")
        long = int(input("How long do you want : "))
        diamond_star(long)
    elif(choice == 8):
        print(10*"=",menu[choice-1],10*"=")
        long = int(input("How long do you want : "))
        hourglass_star(long)
    else:
        print("Sorry your choice nothing in the list")
