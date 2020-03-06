import menus

def main_menu():
    while True:
        title = "MENU"
        main_menus = ["Star Shape","Calculator Menu"]
        exit = ["Exit"]
        menu = main_menus + exit
        print(10*"=",title,10*"=")
        for i in range(0,len(menu)):
            print(i+1, menu[i])
        choice = int(input("Choice your menu : "))
        print(50*"=")
        if(choice == 1):
            print(10*"=",menu[choice-1],10*"=")
            menus.star_shape()
        elif(choice == 2):
            print(10*"=",menu[choice-1],10*"=")
            print("Comming Soon")
        elif(choice == 3):
            print(10*"=",menu[choice-1],10*"=")
            menus.exit_menu()
        else:
            print("Sorry your choice nothing in the list")

main_menu()