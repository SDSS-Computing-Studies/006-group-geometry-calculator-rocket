#!python3
# Volume Calculator
# Feel free to rename your variables


def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Lj
    # Modified: Lj fernandez
    # title
    print("=======================")
    print("=======================")
    print("===Volume calculator===")
    print("=======================")
    print("=======================")
    e=input("Press The Enter Key to Begin")

    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Lj
    # Modified: Lj Fernandez
    print("choose any shape from this category: Triangle, Rectangle, Circle, Square")
    a=input(">>>")
    pass

def squareArea():
    print("Type any number for 1")
    t=input(">>>")
    t=int(t)
    t=(t**2)
    print (t)

def circleArea():
    print("Type any Number for 1")
    t=input(">>>")
    t=int(t)
    t=(math.pi * t**2)
    print(t)

def triangleArea():
    print("Type any Number for 1")
    t=input(">>>")
    print("Type any Number for 2")
    f=input(">>>")
    t=int(t)
    f=int(f)
    t=(t*f/2)
    print(t)

def rectangleArea():
    print("Type any Number for 1")
    t=input(">>>")
    print("Type any Number for 2")
    f=input(">>>")
    t=int(t)
    f=int(f)
    t=(t*f)
    print(t)

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit

     quit = False  
      title()

    while quit == False:
        instructions()
        a=input(">>> ")
        if a =="Square":
            squareArea()
        elif a =="Circle":
            circleArea()
        elif a =="Triangle":
            triangleArea()
        elif a =="Rectangle":
            rectangleArea()
        else:
            print ("Invaild, Choose a Shape!")
        
        if a == "q":
            print("Are You Sure to Quit?\n Press C to Continue\n Press Q to Quit")
            menu=input(">>>")
            if menu == "c""C":
                instructions()
            elif menu == "q""Q":
                print ("later!!!")
                quit == True
            break

main()




