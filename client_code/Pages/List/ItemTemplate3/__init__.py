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
        self.init_components(**properties)

    def list_link_click(self, **event_args):
        name = self.list_link.text
        print(f"This is the name of the list: {name}")
        self.open_gift_page(name)

    def open_gift_page(self, name):
        # Assuming there's a server call to get the list based on its name
        list_row = anvil.server.call('get_list_name', name)

        if list_row is not None:
            # Use the ID of the retrieved list row
            list_id = list_row['ID']

            # Now, you can use the get_list_by_id function to get the list by ID
            list_data = anvil.server.call('get_list', list_id)

            if list_data is not None:
                routing.set_url_hash(url_pattern='Gift', url_dict={'List_ID': list_id})
            else:
                alert(f"No matching list found for ID: {list_id}")
        else:
            alert(f"No matching list found for name: {name}")


  

