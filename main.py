

# author : Itay Gabzo

# a method for adding two numbers
def addition(num1,num2):
    print(num1+num2)


def subtraction(num1, num2):
    print(num1-num2)


def multification(num1,num2):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def division(num1,num2):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def power(num1,num2):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while true:
        print("welcome to the calculator!\n"
              "you have the following mathematical actions:\n"
                "a - addtion\n"
                "s - subtraction\n"
                "m - multification\n"
                "d - division\n"
                "p - power")

        action = input("enter the desiered action: ")
        valid = false
        match action:
            case 'a':
                while not valid:
                    try:
                        num1 = float(input("enter a number: "))
                        num2 = float(input("enter a number: "))
                        valid = true
                        addition(num1, num2)
                    except:
                        print("Invalid input please try again")
            case 's':
                while not valid:
                    try:
                        num1 = float(input("enter a number: "))
                        num2 = float(input("enter a number: "))
                        valid = true
                        subtraction(num1, num2)
                    except:
                        print("Invalid input please try again")
