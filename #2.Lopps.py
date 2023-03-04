blockchain = [[19]]


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount):

    blockchain.append([get_last_blockchain_value(), transaction_amount])


def get_transaction_value():
    """Returns the input of a new transaction value as a float"""
    user_input = float(input("Your transaction amount: "))
    return user_input


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


def print_blockchain():
    for block in blockchain:
        print("Outputting block")
        print(block)


while (True):
    print("Please choose!")
    print("1. Add a new transaction value!")
    print("2. Output the the blockchain blocks!")
    user_choice = get_user_choice()
    if user_choice == "1":
        user_value = get_transaction_value()
        add_value(user_value)
    elif user_choice == "2":
        print_blockchain()
    else:
        print("Do you want to quit?")

print("done")
