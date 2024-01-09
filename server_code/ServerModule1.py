import anvil.users
from anvil import *
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

selected_list_name = None

@anvil.server.callable
def add_gift(task_info):

  user = anvil.users.get_user()

  url_parameters = routing.get_url_hash()
  list_name = url_parameters.get('List_Name')


  if not user: 
    return
    
  # Add the current user as the 'user' link to the gift
  #task_info['user'] = user

 # app_tables.gift['User'] = user
  #how to add whhat user is logged in to the gift tabel
  app_tables.gift.add_row(**task_info)
  pass

@anvil.server.callable
def get_gift(list_name=None):

    user = anvil.users.get_user()

    if not user:
        return

    if list_name:
        return app_tables.gift.search(List_Name=list_name)
    else:
        return app_tables.gift.search()

@anvil.server.callable
def get_list_name(name): 
    # Query the 'Wishlist' table to find a row where the 'Name' column matches the provided name
  result = app_tables.wishlist.search(q.name == name)

    # Check if a matching row was found
  if len(result) == 1:
      return result[0]  # Return the matching row
  else:
      return None  # Return None if no matching row was found
  

@anvil.server.callable
def add_list(task_info):
    user = anvil.users.get_user()

    if not user: 
        return

    task_info['User_Email'] = user

    app_tables.wishlist.add_row(**task_info)
  
@anvil.server.callable
def get_list():
    user = anvil.users.get_user()

    if not user:
        return []

    # Get the row for the current user
    user_row = app_tables.users.get(email=user['email'])

    # Return the wishlists associated with the user
    return app_tables.wishlist.search(User_Email=user_row)


@anvil.server.callable
def delete_gift(gift):
  gift.delete()
