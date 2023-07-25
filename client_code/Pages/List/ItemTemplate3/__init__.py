from ._anvil_designer import ItemTemplate3Template
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate3(ItemTemplate3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def list_link_click(self, **event_args):
        # Get the name of the list from the link's text
      Name = self.list_link.text

        # Call the 'open_gift_page' method
      self.open_gift_page(Name)
    
  def open_gift_page(self, Name):
    # Navigate to the Gift page with the list name as a URL parameter
    open_form('Pages.Gift', Name = Name, open_in_new_tab=True )


    
  pass


  

