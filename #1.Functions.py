blockchain = [[19]]


def add_value(transaction_amount):
    blockchain.append([blockchain[-1],transaction_amount])
    print(blockchain)

add_value(10)
add_value(12)
add_value(32)

