lst = ['Apple ' ,'Guava' , 'mango' ,'banana', 'kivi' ]

print("length of list:" ,  len(lst))
print("first element:" ,  lst[0])
print("last element:" ,  lst[-1])

lst.append ('Papaya')
print("Updated list:" , lst)

lst.remove ('Guava')
print("Updated list:" , lst)

lst.sort()
print("sorted list:" , lst)

lst.pop(1)
print("Updated list:" , lst)

lst.reverse()
print("reverse list:" , lst)


print("Multiplication on list:" , lst* 2)

lst = lst [:4]
print("sliced list:" , lst)

lst.clear()
print("Updated list:" , lst)

