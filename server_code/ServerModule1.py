import anvil.users
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42

@anvil.server.callable
def add_gift(task_info):

  user = anvil.users.get_user()

  if not user: 
    return

 # app_tables.gift['User'] = user
  #how to add whhat user is logged in to the gift tabel
  app_tables.gift.add_row(**task_info)
  pass

@anvil.server.callable
def get_gift():

  user = anvil.users.get_user()

  if not user:
    return
  
  return app_tables.gift.search(tables.order_by('GiftId', acending=False))
  #rows = app_tables.gift.search()

    # Convert the rows to a list of dictionaries
  #$data = []
  #for row in rows:
  #    data.append({
  #        'Name': row['Name'],
  #        'Description': row['Description'],
  #        'URL': row['URL'],

          # Add more columns as needed
  #    })

  #return data
  
  pass

