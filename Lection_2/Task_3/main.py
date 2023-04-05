print ("use a space to separate the elements of the list")

set1 = set(input("Enter the first set of elements: ").split())
set2 = set(input("Enter the second set of elements: ").split())
set3 = set(input("Enter the third set of elements: ").split())

dubl_el_set1 = set(filter(lambda x: x in set2 or x in set3, set1))
dubl_el_set2 = set(filter(lambda x: x in set1 or x in set3, set2))
dubl_el_set3 = set(filter(lambda x: x in set1 or x in set2, set3))

result = dubl_el_set1.union(dubl_el_set2, dubl_el_set3)

print("Non-unique elements from all sets: ", result)