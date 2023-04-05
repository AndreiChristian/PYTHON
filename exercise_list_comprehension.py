simple_list = [1, 2, 3, 4, 5]
doubled_list = []
for el in simple_list:
    doubled_list.append(el * 2)

# print(doubled_list)

comprehension_list = [el*2 for el in simple_list]
# print(comprehension_list)

conditional_list = [el * 2 for el in simple_list if el>3 ]

print(conditional_list)