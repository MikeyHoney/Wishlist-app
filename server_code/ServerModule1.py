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

  if not user: 
    return
    
  # Add the current user as the 'user' link to the gift
  #task_info['user'] = user

 # app_tables.gift['User'] = user
  #how to add whhat user is logged in to the gift tabel
  app_tables.gift.add_row(**task_info)
  pass

@anvil.server.callable
def get_gift():

  user = anvil.users.get_user()

  if not user:
    return

  return app_tables.gift.search()
  
  pass

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
  #print(f"user: {user.email}")

  if not user: 
    return
  # Set the user's email as part of the task_info dictionary
  #task_info['User_Email'] = user.email


  app_tables.wishlist.add_row(**task_info)
  pass
  
@anvil.server.callable
def get_list():

  user = anvil.users.get_user()

  if not user:
    return
  
  return app_tables.wishlist.search(User_Email=anvil.users.get_user(['email']))
  #return app_tables.wishlist.search(
  #      q.any_of(
  #        {'User_Email': user.email}
  #      )
  #  )


  pass

@anvil.server.callable
def delete_gift(gift):
  gift.delete()
