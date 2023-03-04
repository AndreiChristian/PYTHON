blockchain = [[19]]


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount):

    blockchain.append([get_last_blockchain_value(), transaction_amount])


user_amount = float(input("Your transaction amount:  "))
add_value(transaction_amount=(user_amount))
add_value(10)
add_value(transaction_amount=12)
add_value(32)

for block in blockchain:
    print("Outputting block")
    print(block)
