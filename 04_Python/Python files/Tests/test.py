import csv

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
job_title = input("Enter job title: ")
company = input("Enter company: ")

data = []

# while True:
#     company = input("enter value4 ")
#     if company.upper() == "Q":
#         break
#     data.append([first_name, last_name, job_title, company])

with open('test.csv', 'a+') as file:
    my_dictionary = csv.writer(file)
    my_dictionary.writerow(["First name", "Last name", "Job title", "Company"])
    my_dictionary.writerow([first_name, last_name, job_title, company])
    for row in data:
        my_dictionary.writerow(row)
    print(my_dictionary)

