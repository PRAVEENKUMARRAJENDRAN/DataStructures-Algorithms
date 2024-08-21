s = set()
print(s)

s = set([1,2,3])
print(s)

s = set(list([1,2]))

s.add(4)
print(s)

# discard2 2 if it is present in the set
s.discard(2)
print(s)
s.remove(4)
print(s)

s.pop()
print(s)



names1 = set(["Glory", "Tony", "Joel", "Dennis"])
names2 = set(["Morgan", "Joel", "Tony", "Emmanuel", "Diego"])
print(names1.union(names2))
print(names1 | names2)

print(names1.intersection(names2))
print(names1 & names2)

print(names2.difference(names1))