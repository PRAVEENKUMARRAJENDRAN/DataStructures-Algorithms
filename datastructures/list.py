mylist = list()


# mutable,ordered, contians duplicate.
mylist.append(5)
mylist.append(6)
mylist.append(1)
mylist.append(1)

mylist2 = mylist
#Removes all element from the list 
#mylist.clear()
# add the element in the list
mylist.extend([1,2,3,4])

mylist.insert(0, 2)
mylist.pop(4)


print(mylist)
print(mylist2)



