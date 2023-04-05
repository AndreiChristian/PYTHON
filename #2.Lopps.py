blockchain = []


def get_last_blockchain_value():
    """Returns the last value of the current blockchain and returns None if there is no value"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_value):
    """Append a new value as well as the last blockchain value to the blockchain as a new element in the list """
    if (last_value == None):
        last_value = 1
    blockchain.append([last_value, transaction_amount])


def get_transaction_value():
    """Returns the input of a new transaction value as a float"""
    user_input = float(input("Your transaction amount: "))
    return user_input


def get_user_choice():
    """Returns the input of the user (new transaction or print blockchain)"""
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
    print("h: Manipulate the chain!")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        user_value = get_transaction_value()
        add_value(transaction_amount=user_value,
                  last_value=get_last_blockchain_value())
    elif user_choice == "2":
        print_blockchain()
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = 2
    elif user_choice == "q":
        break
    else:
        print("Invalid input!")

print("done")
