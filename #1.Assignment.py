# create a function that takes your name and age and returns it as a string

def nameAndAgeToString():
    """a function that asks the user for their name and age, turns the age to 
    string and prints the two of them combined"""

    userName = input("What is your name? ")
    userAge = input("What is your age? ")
    print("Your name is " + userName + " and you are " + userAge + " years old")


def stringConvertor(arg_1=input("Please enter the first argument "),
                    arg_2=input("Please enter the secod argument ")):
    """
    a function that takes two arguments, converts them to string and prints the result
    """
    print(str(arg_1), str(arg_2))


def numberOfDecadesLived(age=float(input("How old are you? Please enter the input in y.o. :"))):
    decades = int((age - age%10)/10)
    print("You lived " + str(decades) + " decades !")


nameAndAgeToString()
stringConvertor(arg_1=3.4, arg_2=6)
stringConvertor()
numberOfDecadesLived()

