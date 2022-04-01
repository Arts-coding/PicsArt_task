
entries = []

entries_list = []


def adding(add_content):
    entries.append(add_content)


def get_entries():
    return entries
    
def del_entry(id_entry):
    if  0 <= id_entry - 1  <= len(entries):
         entries.pop(id_entry -1)
    else:
        print("There isn't that entry")

def adding_list(add_list):
    entries.append([add_list])
    print(entries)
  

