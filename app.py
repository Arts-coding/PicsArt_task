from datetime import datetime
from database import adding, del_entry, get_entries,adding_list

menu = """
Please select one of the following option:
1.  Add new string.
2.  View entries.
3.  Delate.
4.  Add list.
5.  Exit.

Your selection:  """

welcome = "Welcome!"


print(welcome)


while(user_input := input(menu)) != "5":
    if user_input == "1":
        add_content = input('Add string ')
        add_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        
        if add_content != '':
            adding(add_content)
        else:
            print('Please add new entry')

    if user_input == "2":
        entries = get_entries()
        if entries == [ ]:
            print('Empty!')
        else:
            for entry in entries:
                print(entry)

    if user_input == "3":
        id_entry = int(input('Which one?  '))
        del_entry(id_entry)
    
    if user_input == "4":
        add_list = input('Add list item ')
        add_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        adding_list(add_list)

