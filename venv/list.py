l=[1,2,3,4,5,6,1,2,3]
#adding new element at the end
print("Append(list.append())")
l.append(10)
print(l)
#inserting at a particular index
print("inserting at a particular index (list.index(element,index))")
l.insert(2,200)
print(l)
#removing 200
print('removing the particular element from the list (list.remove(element))')
l.remove(200)
print(l)
#poping the last element
print('printing the last inserted element(list.pop())')
l.pop()
print(l)
#getting the index of a particular element
print("Getting the inedex of the element(list.index(element))")
print(l.index(4))
#sorting the list
print('Sorting the list(list.sort())')
l.sort()
print(l)
#reversing the list
print('Reversing th list(lisr.reverse())')
l.reverse()
print(l)
#counting the no of elements
print('Getting the no of elements in the list(len(list))')
print(len(l))
#counting the no of occurence of 2
print('Counting the frequency of a particular character(l.count(element))')
print(l.count(2))
