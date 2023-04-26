num_sets = int(input("Enter the number of sets: "))
print("Use a space to separate the elements of the sets")
sets = []

for сount in range(num_sets):
    new_sets = set(input("Enter the elements of set " + str(сount+1) + ": ").split())
    sets.append(new_sets)

duplicate_elements = set()
for set_activ in range(num_sets):
    for set_next in range(set_activ+1, num_sets):
        duplicate_elements.update(sets[set_activ].intersection(sets[set_next]))
        
print("Non-unique elements from all sets: ", duplicate_elements)