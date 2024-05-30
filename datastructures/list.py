l =  list()

l.append(0)

l2 = [1,2,3,4]

#add the l2 list to l1
l.extend(l2)
print(l)

#insert 
#first argumnet is the index and second is the value 
l.insert(4,2)
print(l)

#remove
#Remove the element from the list
#if it has many element it will remove the first one
l.remove(2)
print(l)