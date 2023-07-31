from ._anvil_designer import ItemTemplate3Template
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing



class ItemTemplate3(ItemTemplate3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def list_link_click(self, **event_args):
        # Get the name of the list from the link's text
    name = self.list_link.text
    anvil.server.call('set_selected_list_name', name)
    print(f"This is the name of the list: {name}")


        # Call the 'open_gift_page' method
    self.open_gift_page(name)
    
  def open_gift_page(self, name):
    # Navigate to the Gift page with the list name as a URL parameter
    routing.set_url_hash('Gift', list_name=name)


    
  pass


  

