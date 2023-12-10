

# author : Itay Gabzo

#
def addition(num1,num2):
    if(type(num1) is int or type(num1) is float):
        if(type(num2) is int or type(num2) is float):
            print(num1+num2)
        else:
            print("Input error")
    else:
        print("Input error")


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
    print("welcome to the calculator!\n"
          "you have the following mathematical actions:\n"
          "a - addtion\n"
          "s - subtraction\n"
          "m - multification\n"
          "d - division\n"
          "p - power")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
