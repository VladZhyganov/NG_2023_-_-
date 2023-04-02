print ("enter 10 elements to form your list - these can be 'int, str, float, bool ")
your_list = []
x = 0
while True:
    input_element = input (("Enter element: "))
    x +=1
    if input_element.isdigit():
        item = int(input_element)
    elif "." in input_element:
        try:
            item = float(input_element)
        except ValueError:
            item = input_element
    elif input_element.lower() == "true" or input_element.lower() == "false":
        item = bool(input_element)
    else:
        item = input_element
    your_list.append(item)
    
    if x==10:
        break
    print("You entered", x, "element.")
print("in you list entered", x, "elements.")
print ("")
print("The final list:", your_list)

print ()
while True:
    print ("to select and determine the number of elements by type from your list, enter the name of the type") 
    a=input("enter 'int, str, float,bool, for exit enter 'quit'")
    if a == "quit":
        print ("Good bay!!!")
        break
    if a=='str':
        type_to_select =str
    if a=='bool':
        type_to_select =bool
    if a=='float':
        type_to_select =float
    if a=='int':
        type_to_select =int

    sel_elements = []

    for element in your_list:
        if type(element) == type_to_select:
                sel_elements.append(element)

    print("selected elements:", a, sel_elements)
    print("how many elements:", len(sel_elements))    