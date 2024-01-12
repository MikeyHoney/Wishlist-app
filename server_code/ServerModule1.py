import anvil.users
from anvil import *
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import uuid



selected_list_id = None

@anvil.server.callable
def add_gift(task_info):
    print(f"Received task_info: {task_info}")
    #print(f"Received list_id: {list_id}")
    user = anvil.users.get_user()

    try:
        task_info['Name'] = user

        task_info['List_Id'] = list_id

        app_tables.gift.add_row(**task_info)
        
        print("Gift added successfully.")
    except Exception as e:
        print(f"Error adding gift: {e}")

@anvil.server.callable
def get_gift(list_id=None):

    user = anvil.users.get_user()

    if not user:
        return

    if list_id:
        if isinstance(list_id, str):
            list_row = app_tables.wishlist.get(ID=list_id)
        elif isinstance(list_id, app_tables.wishlist):
            list_row = list_id
        else:
            return []

        return app_tables.gift.search(List_Id=list_row)
    else:
        return app_tables.gift.search()

@anvil.server.callable
def get_list_name(name): 
    result = app_tables.wishlist.search(Name=name)

    # Check if a matching row was found
    if len(result) == 1:
        return result[0]  # Return the matching row
    else:
        return None 
  

@anvil.server.callable
def add_list(task_info):
    user = anvil.users.get_user()

    if not user: 
        return

    task_info['User_Email'] = user
    task_info['ID'] = uuid.uuid4().int

    app_tables.wishlist.add_row(**task_info)
  
@anvil.server.callable
def get_list(list_id):
    return app_tables.wishlist.get(User_Email==)


@anvil.server.callable
def delete_gift(gift):
  gift.delete()
