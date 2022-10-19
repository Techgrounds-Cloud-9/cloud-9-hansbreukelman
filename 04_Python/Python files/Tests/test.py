my_dictionary = {}
for key in range(1):
    f = input("Enter first name: ")
    l = input("Enter last name: ")
    j = input("Enter job title: ")
    c = input("Enter company: ")

    my_dictionary[f, l, j, c] = l, j, c

    # print(matrix[i][j], end = " ")  


# 👇️ {'Alice': '100', 'Bob': '100', 'Carl': '100'}
# print(key, '->', my_dictionary[key])
print(my_dictionary)
# employees = {}

# for i in range(3):
#     name = input("Enter employee's name: ")
#     salary = input("Enter employee's salary: ")

#     employees[name] = salary

