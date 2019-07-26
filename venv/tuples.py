#tuples are used similar to that of a list but we cant modify the elements in the tuple
a=(1,2,3)
print("we can count the frequency")
print(a.count(1))
print("we can check the presence of some elements")
print(a.__contains__(1))
print('we can unpack intom seperate variables')
x,y,z=a
print(f'x:{x}')
print(f'y:{y}')
print(f'z:{z}')
