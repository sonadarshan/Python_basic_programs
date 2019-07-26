try:
    a=int(input('Enter a'))
    b=int(input('Enter b'))
    print('a/b :')
    print (a/b)
except ValueError:
    print("Special characters are not allowed ")
    exit(0)
except ZeroDivisionError:
    print('Division by 0 is not allowed')
