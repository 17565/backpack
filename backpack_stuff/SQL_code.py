import sqlite3

db_file ="food_backpack.db"

def show_backpack(connection):
    """print backpack"""
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM food"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f'\n{"name":<20}{"description":<20}')
        for item in results:
            print(f"{item[1]:<20}{item[2]:<20}")
    except:
        print("something went wrong with connection")

def add_item(connection, item_name, item_description):
    """add item to backpack database"""
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO food(food_item, cost) VALUES (?,?)"
        cursor.execute(sql,(item_name, item_description))
        connection.commit()
    except:
        print("item could not be add")

def delete_item(connection, item_name, item_description):
    """delete item by name from the database"""
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM food WHERE food_item = ?"
        cursor.execute(sql,(item_name,))
        num_rows_affected = cursor.rowcount
        if num_rows_affected == 0:\
            print("can't find item")
        else:
            connection.commit()
    except:
        print("item dose not exist")

def update_description(connection, item_name, new_cost):
    try:
        cursor = connection.cursor()
        sql = "UPDATE food SET cost = ? WHERE food_item = ?"
        cursor.execute(sql, (new_cost, item_name))
        num_rows_affected = cursor.rowcount
        if num_rows_affected == 0:\
            print("can't find item")
        else:
            connection.commit()
    except:
        print("failed to update the item")

with sqlite3.connect(db_file) as connection:
    
    while True:
        answer = (input("what do you want to do \ntype 1 to print list: \ntype 2 to add item \ntype 3 to delete item \ntype 4 to update item in list \n: "))
        if answer == "1": 
            show_backpack(connection)
        if answer == "2": 
            show_backpack(connection)
            item = (input("what is the item: "))
            description = (input("what is item description: "))
            add_item(connection, item, description)
        if answer == "3":
            show_backpack(connection)
            item = (input("what is the item: "))
            description = (input("what is item description: "))
            delete_item(connection, item, description)
        if answer == "4":
            show_backpack(connection)
            item = (input("what is the item: "))
            cost = (input("what is item description: "))
            update_description(connection, item, cost)


    #show_backpack(connection)
    #update_description(connection, "pizza", "5")
    #show_backpack(connection)