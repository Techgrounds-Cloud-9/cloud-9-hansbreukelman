while True:
    number = int(input('Enter a nummber:'))
    if number == 100:
        name = True
        print('This is the perfect number!')
        break
    elif number < 100:
      print("\nI don't think", number, "is enough!\n")
    else:
        print("\nThat is incorrect,", number, "is too much!\n") 