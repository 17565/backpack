"""backpack"""

def show_backpack():
    """show backpack"""
    print("this is your list {}". format(backpack))

#def add_item(item):
#    '''add a single item to the backpack'''
#    backpack.append(item)

def add_items_to_backpack():
    """add item in to backpack"""
    print("to stop add items type: done")
    while True:
        results = (input("what do you want in your backpack: "))
        if results == "done":
            break
        else:
            backpack.append(results)
            while True:
                try:
                    cost = int(input("what is the cost of this item: $"))
                except ValueError:
                    print("please type a cost")
                else:
                    backpack.append(cost)
                    break

def remove_item_from_backpack():
    """remove a item of choice from the backpack"""
    print(backpack,"if you want to see list agin type: show backpack")
    while True:
        item = (input("what do you want to be deleted from your backpack: "))
        if item == "done":
            break
        elif item == "show backpack":
            print(backpack)
        elif item not in backpack:
            print("item {} not found try again". format(item))
        else:
            backpack.remove(item)
            print("the item {} has been removed from{}". format(item,backpack))
            if item == "done":
                break

#back pack where stuff is stored
backpack = list()
#this is the loop that repeast it and bearks if go is typed
while True:
#ask user question
    opitions = (input("what do you want to do: \n make backpack type: 1 \n delete stuff from backpack type: 2 \n to see backpack type: 3 \n:"))
#add item in to back pack

    if opitions == "1":
        add_items_to_backpack()
        #i = input("What do you want to add? ")
        #add_item(i)

#removes an item from the backpack
    elif opitions == "2":
        remove_item_from_backpack()


#shows items in backpack
    elif opitions == "3":
        show_backpack()
        
    else:
        print("that function {} dose not exist\n ".format(opitions))
#adds item to backpack