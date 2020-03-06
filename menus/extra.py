def exit_menu():
    while True:
        exit = input("Do you want to exit <yes,no>? ")
        exit = exit.lower()
        if (exit == "y") or (exit == "yes"):
            print("Good Bye")
            quit()
        elif (exit == "n") or (exit == "no"):
            # break
        else:
            print("Error")