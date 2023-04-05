nameList = [
    "John", "Mary", "Bob", "Molly", "Sue", "Joe", "Tom", "Sally", "Nancy", "Nathan", "Nathaniel", "Natalie", "Natalia", "Natalie",
]


def nameLength():
    for name in nameList:
        print(f"The length of {name} is equal to {len(name)}")

# nameLength()


def nameLengthLongerThanFive():
    for name in nameList:
        if len(name) > 5:
            print(f"{name} is {len(name)} characters long! ")

# nameLengthLongerThanFive()

def names_with_n_or_N():
    for name in nameList:
        if name.__contains__("n") or name.__contains__("N"):
            print(f"{name} includes 'n' or 'N'.")

names_with_n_or_N()

def empyt_list():
    print("Empyting List")
    while nameList:
        nameList.pop()
    print(f"List is empty. The current list is now just : {nameList} ")

empyt_list()