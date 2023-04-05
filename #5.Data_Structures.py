open_transactions = []
genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": []
}
blockchain = [genesis_block]
owner = "Andrei"


def get_last_blockchain_value():
    """Returns the last value of the current blockchain and returns None if there is no value"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(sender, recipient, amount=1.0):
    """Append a new value as well as the last blockchain value to the blockchain as a new element in the list """
    last_value = get_last_blockchain_value()
    if (last_value == None):
        last_value = 1
    transaction = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    }
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = ""
    for keys in last_block:
        value = last_block[keys]
        hashed_block = hashed_block + str(value)
    print(hashed_block)
    block = {
        "previous_hash": "XYZ",
        "index": len(blockchain),
        "transactions": open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    """Returns the input of a new transaction value as a float"""
    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Your transaction amount: "))
    return (tx_recipient, tx_amount)


def get_user_choice():
    """Returns the input of the user (new transaction or print blockchain)"""
    user_input = input("Your choice: ")
    return user_input


def print_blockchain():
    for block in blockchain:
        print("Outputting block")
        print(block)
    else:
        print("-"*20)


def verify_chain():
    """Verify the current blockchain and return True if it's valid, False otherwise"""
    print("Verifying Blockchain")
    index = 0
    is_valid = True
    for block in blockchain:
        if index == 0:
            index += 1
            continue
        if block[0] == blockchain[index-1]:
            is_valid = True
        else:
            is_valid = False
            break
        index += 1
    return is_valid


waiting_for_input = True


while (waiting_for_input):
    print("Please choose!")
    print("1. Add a new transaction value!")
    print("2. Mine a new block!")
    print("3. Output the the blockchain blocks!")
    print("h: Manipulate the chain!")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_value(sender=owner, recipient=recipient, amount=amount)
        print(open_transactions)
    elif user_choice == "2":
        mine_block()
    elif user_choice == "3":
        print_blockchain()
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = 2
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Invalid input!")
    # if not verify_chain():
    #     print("Invalid blockchain!")
    #     break
else:
    print("user left!")

print("done")
