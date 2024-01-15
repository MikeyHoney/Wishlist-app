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
def add_gift(task_info, list_id):
    print(f"Received task_info: {task_info}")
    print(f"Received list_id: {list_id}")
    user = anvil.users.get_user()

    try:
        # task_info['Name'] = user
        # task_info['List_Id'] = list_id

        # Fetch the Wishlist record
        wishlist_row = app_tables.wishlist.get(List_Id=list_id)
        if not wishlist_row:
            raise Exception(f"No matching wishlist found for ID: {list_id}")

        task_info['List_Id'] = wishlist_row
        print(f"Received task_info: {task_info['List_Id']}")

        new_gift = app_tables.gift.add_row(**task_info)
        
        print("Gift added successfully.")
    except Exception as e:
        print(f"Error adding gift: {e}")
        return None  # Return None in case of an error

    return new_gift

@anvil.server.callable
def get_gift(list_id=None):

    user = anvil.users.get_user()

    if not user:
        return

    if list_id:
        if isinstance(list_id, str):
            list_row = app_tables.wishlist.get(List_Id=list_id)
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

    if len(result) == 1:
        return result[0] 
    else:
        return None 
  

@anvil.server.callable
def add_list(task_info):
    user = anvil.users.get_user()

    if not user: 
        return

    task_info['User_Email'] = user
    task_info['List_Id'] = str(uuid.uuid4())

    new_list = app_tables.wishlist.add_row(**task_info)

    return new_list
  
@anvil.server.callable
def get_list():

  user = anvil.users.get_user()

  if not user:
    return
  
  return app_tables.wishlist.search(User_Email=anvil.users.get_user(['email']))

@anvil.server.callable
def get_list_with_gifts(list_id):
    #printing
    wishlist_rows = list(app_tables.wishlist.search())
    #print("All Wishlist rows:", wishlist_rows)
    #print("list id: ", list_id)
    #print("This is the searched id: ", app_tables.wishlist.get(List_Id=list_id))

    user = anvil.users.get_user()

    if not user:
        return None


  
    list_row = app_tables.wishlist.get(List_Id=list_id)
  
    #if list_row:
      #print("List Row Contents:", list_row)

    if not list_row:
        return None

    gifts = app_tables.gift.search(List_Id=list_row)


    return {
        'list_info': list_row,
        'gifts': gifts,
    }


@anvil.server.callable
def delete_gift(gift):
  gift.delete()
  
@anvil.server.callable
def open_edit_form(list_id):
    # Fetch the list details
    list_row = app_tables.wishlist.get(List_Id=list_id)
    if list_row:
        # Open the edit form with the list details
        return list_row
    else:
        return None

def update_gift_details(gift_id, name, description, url):
    # Fetch the gift row
    gift_row = app_tables.gift.get(id=gift_id)
    if gift_row:
        # Update gift details
        gift_row.update_row(Name=name, Description=description, URL=url)
        return True
    else:
        return False

