password = ''
while password != 'pass123':
    password = input("Enter password: ")
    if password == 'pass123':
        print("success login")
    else:
        print('try again')
