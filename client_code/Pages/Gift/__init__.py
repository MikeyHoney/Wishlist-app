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


from anvil_extras import routing
@routing.route('Gift', url_keys=['Name'])
class Gift(GiftTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.repeating_panel.set_event_handler('x-delete', self.delete_gift)
     
    self.List_Name = None  # Initialize the current_list_name variable
  
  def delete_gift(self, gift, **event_args):
  

    # Call the server function to delete the gift row by its name
    anvil.server.call('delete_gift', gift)

    self.repeating_panel.items = anvil.server.call('get_gift')
    
  
  def form_show(self, **event_args):
    
    #self.repeating_panel.items = anvil.server.call('get_gift')
     gifts = anvil.server.call('get_gift', list_name=self.List_Name)
     self.repeating_panel.items = gifts


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

    # Get the list name from the URL parameters
    list_name = routing.get_url_hash().get('List_Name', None)

    if list_name is not None:
        print(f"This is the name of the list: {list_name}")

        AddGift = {}
        AddGift['Name'] = self.Name.text
        AddGift['Description'] = self.Description.text
        AddGift['URL'] = self.URL.text
        AddGift['User_Email'] = anvil.users.get_user()['email']
        AddGift['List_Name'] = list_name

        anvil.server.call('add_gift', AddGift)
        self.form_show()
    else:
        alert("No matching list found in the URL parameters.")