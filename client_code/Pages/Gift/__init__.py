from ._anvil_designer import GiftTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Gift(GiftTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def form_show(self, **event_args):
    self.repeating_panel.items = anvil.server.call('get_gift')


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
