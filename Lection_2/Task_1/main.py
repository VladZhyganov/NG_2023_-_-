your_list = []
for i in range(5):
    element = input(f"Enter element {i+1}: ")
    if element.isdigit():
        your_list.append(int(element))
    elif "." in element:
        try:
            your_list.append(float(element))
        except ValueError:
            your_list.append(element)
    elif element.lower() == "true" or element.lower() == "false":
        your_list.append(bool(element))
    else:
        your_list.append(element)

print(f"Your list contains {len(your_list)} elements: {your_list}")

while True:
    typ = input("Enter a data type ('int', 'str', 'float', 'bool') to select elements, or 'quit' to exit: ")
    if typ == "quit":
        print("Goodbye!")
        break
    selected_elements = [e for e in your_list if type(e).__name__ == typ]
    print(f"Selected elements of type {typ}: {selected_elements}")
    print(f"Number of elements of type {typ}: {len(selected_elements)}")