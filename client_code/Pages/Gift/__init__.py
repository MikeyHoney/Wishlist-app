from ._anvil_designer import GiftTemplate
#from .NavBar import NavBar  # Import the NavBar custom component
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import open_form




from anvil_extras import routing
@routing.route('Gift')
class Gift(GiftTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.repeating_panel.set_event_handler('x-delete', self.delete_gift)
     
    self.List_Name = None  # Initialize the current_list_name variable
  
  def delete_gift(self, gift, **event_args):
     # Get the 'Name' value from the gift row
    #gift_name = gift['Name']

    # Call the server function to delete the gift row by its name
    anvil.server.call('delete_gift', gift)

    # Refresh the repeating panel to update the UI
    self.repeating_panel.items = anvil.server.call('get_gift')
    #self.refresh_items()
    
  def set_List_Name(self, List_Name):
    self.List_Name = List_Name
  
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
      
    user = anvil.users.get_user('')

    AddGift = {}
    AddGift['Name'] = self.Name.text
    AddGift['Description'] = self.Description.text
    AddGift['URL'] = self.URL.text
    AddGift['User_Email'] = anvil.users.get_user('email')
    AddGift['List_Name'] =  self.List_Name


    anvil.server.call('add_gift', AddGift)
    pass

  #def list_link(self, **event_args):
    #open_form('Pages.List')