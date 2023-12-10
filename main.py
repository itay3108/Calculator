

# author : Itay Gabzo

# a method for adding two numbers
def addition(num1,num2):
    print(num1+num2,"\n")


# a method for substracting two numbers
def subtraction(num1, num2):
    print(num1-num2,"\n")


# a method for multiplying two numbers
def multification(num1,num2):
    print(num1*num2,"\n")



def division(num1,num2):
    if num2 != 0:
        print(num1/num2,"\n")
    else:
        print("can't divide by zero")


def power(num1,num2):
    try:
        print(pow(num1,num2,float),"\n")
    except:
        print("Value Error(number too large)")

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

            case 'm':
                while not valid:
                    try:
                        num1 = float(input("enter a number: "))
                        num2 = float(input("enter a number: "))
                        valid = true
                        multification(num1, num2)
                    except:
                        print("Invalid input please try again")

            case 'd':
                while not valid:
                    try:
                        num1 = float(input("enter a number: "))
                        num2 = float(input("enter a number: "))
                        valid = true
                        division(num1,num2)
                    except:
                        print("Invalid input please try again")

            case 'p':
                while not valid:
                    try:
                        num1 = float(input("enter a number: "))
                        num2 = float(input("enter a number: "))
                        valid = true
                        power(num1,num2)
                    except:
                        print("Invalid input please try again")

