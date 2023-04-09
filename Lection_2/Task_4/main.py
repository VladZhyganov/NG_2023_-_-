card_index = []
while True:
  
    print ("enter next action - \n"
           "add new book press - 'add'\n"
           "show card index - 'show'\n"
           "delete book - 'del'\n"
           "find book - 'find'\n"
           "edit book - 'edit', or 'quit' for exit")
    action = input("enter next action - "  )
    if action == "quit":
        print("Goodbye!")
        break
    elif action =="add":
        new_book = {}
        name_book = input("name_book: ")
        new_book['name_book'] = name_book
        avtor = input("avtor: ")
        new_book['avtor'] = avtor
        year_published = input("year_published: ")
        new_book['year_published'] = year_published
        number_of_pages = input("number_of_pages: ")
        new_book['number_of_pages'] = number_of_pages
        ganre = input("ganre: ")
        new_book['ganre'] = ganre
        
        binding = input("binding 'soft or hard': ")
        if binding =="soft":
            soft=binding
            new_book['binding'] = soft
        elif binding =="hard":
            hard=binding
            new_book['binding'] = hard
        print(f"{new_book} has been added to the index.")
        card_index.append(new_book)
    if action == "show":
        print ("--------------------------------------------------------------------------------------------------------------")
        print ("YOUR card_index")
        print ("--------------------------------------------------------------------------------------------------------------")
        print (card_index)    
        print ("--------------------------------------------------------------------------------------------------------------")
  
    elif action == "del":
        name_book = input("Enter the name of the book to delete: ")
        for book in card_index:
            if book['name_book'] == name_book:
                card_index.remove(book)
                print(f"{name_book} has been deleted from the index.")
                break
        else:
            print(f"{new_book} was not found in the index.")

    elif action == "find":
        name_book = input("Enter the name of the book to search for: ")
        for book in card_index:
            if book['name_book'] == name_book:
                print(f"{book['name_book']}, by {book['avtor']}. Published in {book['year_published']}. {book['number_of_pages']} . Ganre: {book['ganre']}")
                break
        else:
            print(f"{name_book} was not found in the index.")

    elif action == "edit":
        name_book = input("Enter the name of the book to edit: ")
        for book in card_index:
            if book['name_book'] == name_book:
                print(f"Which parameter would you like to edit for {name_book}?\n"
                      "- 'name_book' to edit the name\n"
                      "- 'avtor' to edit the author\n"
                      "- 'year_published ' to edit the year published\n"
                      "- 'number_of_pages' to edit the number of pages\n"
                      "- 'ganre' to edit the ganre\n"
                      "- 'binding' to edit the binding\n"
                      "- 'cancel' to cancel")
                parameter = input("Parameter: ")
                if parameter == "cancel":
                    break
                new_value = input(f"Enter new value for {parameter}: ")
                book[parameter] = new_value
                print(f"{name_book} has been updated with the new {parameter} '{new_value}'.")
                break
        else:
            print(f"{name_book} was not found in the index.")

print (card_index)