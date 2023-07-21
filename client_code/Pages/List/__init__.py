from ._anvil_designer import ListTemplate
from anvil import *
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from anvil_extras import routing
@routing.route('List')

class List(ListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    gift_data = anvil.server.call('get_gift')
     # Populate the Data Grid with the gift data
    self.data_grid.items = gift_data
        # Populate the Data Grid with the gift data

  def add_gift_click(self, **event_args):
    
    if not self.Name.text:
      alert("You must enter a name!")
      return
    
    # Description
    if not self.Description.text:
      alert("You must enter a description!")
      return
      
    # URL
    if not self.URL.text:
      alert("You must enter a URL!")
      return
    
    AddGift = {}
    AddGift['Name'] = self.Name.text
    AddGift['Description'] = self.Description.text
    AddGift['URL'] = self.URL.text
    anvil.server.call('add_gift', AddGift)
    pass