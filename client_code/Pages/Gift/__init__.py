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





class Gift(GiftTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

     # Add the NavBar custom component to the form
    #self.nav_bar = NavBar()
    #self.add_component(self.nav_bar)
        
        # Update the NavBar visibility based on user login status
    #user = anvil.users.get_user()
    #self.nav_bar.update_links()
    #self.nav_bar.visible = bool(user)
    
    self.List_Name = None  # Initialize the current_list_name variable

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

  def list_link(self, **event_args):
    open_form('Pages.List')