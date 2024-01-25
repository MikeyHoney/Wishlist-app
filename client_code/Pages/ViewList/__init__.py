from ._anvil_designer import ViewListTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from anvil_extras import routing
@routing.route('ViewList', url_keys=['List_Id'], title="ViewList")
class ViewList(ViewListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    #form show from gifts page to display gifts
  def form_show(self, **event_args):
      url_dict = routing.get_url_dict()

      url_parameters = routing.get_url_hash()
        
      list_id = url_dict.get('List_Id')


      
      if list_id is not None:
            self.List_Id = list_id
            #there are two server calls here fix this
            gifts = anvil.server.call('get_gift', list_id=list_id)
            list_info = anvil.server.call('get_list_with_gifts', list_id)

            if gifts and list_info:
                self.repeating_panel.items = gifts
                label_list = self.label_list
                label_list.text = f"List Name: {list_info['list_info']['Name']}"
                
            else:
                self.repeating_panel.items = [] 
                self.add_gift_button.visible = True
                self.no_gifts_label.text = "No gifts have been added to the list."
      else:
            alert("No matching list found in the URL parameters.")
            routing.set_url_hash('')  
