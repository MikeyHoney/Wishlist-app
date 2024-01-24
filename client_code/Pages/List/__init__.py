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
@routing.route('List', title="Wishlist")
class List(ListTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        #self.repeating_panel.items = anvil.server.call('get_list', list_id=my_list_id)

    def add_list_click(self, **event_args):
        if not self.List_Name.text:
            alert("You must enter a name for your list!")
            return
    
        user = anvil.users.get_user('')
    
        AddList = {}
        AddList['Name'] = self.List_Name.text
        AddList['User_Email'] = anvil.users.get_user('email')
    
        new_list = anvil.server.call('add_list', AddList)
        if new_list:
          routing.set_url_hash(   , url_dict={'List_Id': new_list['List_Id']})
        else:
          alert("Failed to create the list.")
          routing.set_url_hash('Gift', url_dict={'List_Id': new_list['List_Id']})
        
        self.form_show()

    def form_show(self, **event_args):
        #self.repeating_panel.items = anvil.server.call('get_list', list_id=my_list_id)
        self.repeating_panel.items = anvil.server.call('get_list')



    





  




  
