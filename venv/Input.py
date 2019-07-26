#input() function  returns the string always and if we have to take integer input then we have to use int(input)




#Integer input
n=int(input('Enter the integer : '))
print(f'The Entered integer is {n}')


#Float input
f=float(input('Enter the float : '))
print(f'The Entered float is {f}')


#String input
s=input('Enter the string : ')
print(f'The Entered string is {s}')


#Multiple words
first_name,last_name=input('Enter the name in the format (Firstname Lastname) : ').split(' ')
print(f'Fisrt name : {first_name}\nLast name : {last_name}')


#Getting input to the list
print('Entering the values into the list : ')
l=[]
n=int(input('Enter the no of values in the list : '))
for i in range(n):
    l.append(input('Enter the number : '))
print(f'The entered list is {l}')

