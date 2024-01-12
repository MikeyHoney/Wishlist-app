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

        #list_name = self.list_link.text
        #list_name = event_args['sender'].text

        print("list_link_click method triggered")
        #list_name = self.item['Name']
        list_name = self.list_link.text
        print(f"This is the name of the list: {list_name}")
        list_id = self.item['List_Id'] 
        print(f"This is the ID of the list: {list_id}")
        self.open_gift_page(list_id)


    def open_gift_page(self, list_id):
        print(f"open_gift_page method called with list_id: {list_id}")

        result = anvil.server.call('get_list_with_gifts', list_id)

        print(f"this is the result: {result}")


        if result:
            list_info = result['list_info']
            gifts = result['gifts']

            if list_info and gifts:
                routing.set_url_hash(url_pattern='Gift', url_dict={'List_Id': list_info['List_Id']})
            else:
                alert(f"No matching list found for ID: {list_id}")
        else:
            alert(f"No matching list found for ID: {list_id}")


  

