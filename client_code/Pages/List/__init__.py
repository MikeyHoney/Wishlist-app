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
  
  def add_list_click(self, **event_args):
    if not self.List_Name.text:
      alert("You must enter a name for your list!")
      return    
      
    user = anvil.users.get_user('')

    AddList = {}
    AddList['Name'] = self.List_Name.text
    AddList['User_Email'] = anvil.users.get_user('email')
    
    #got to find out how to add linking fields
    anvil.server.call('add_list', AddList)
      
    pass

  def form_show(self, **event_args):
    self.repeating_panel.items = anvil.server.call('get_list')
    





  




  
