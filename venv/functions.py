#general syntax
#function overloading is not possible in python
#def function1():
 #   print("printing in function 1")
def function1(n):
  print(f'printing in function 2: {n}')
def square(a):
    return a*a
def add(first,second):
    return first**second


#function1()
function1(2)
print(square(3))
print(add(second=2,first=3))
#keyword argumements
print(add(3,2))
#positional arguments