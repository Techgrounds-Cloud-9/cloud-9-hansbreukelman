import csv

with open('test.csv', 'a+') as file:
    my_dictionary = csv.writer(file)
    my_dictionary.loc(0,["First name", "Last name", "Job title", "Company"])
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    job_title = input("Enter job title: ")
    company = input("Enter company: ")
    my_dictionary.writerow([first_name, last_name, job_title, company])
    print(my_dictionary)

