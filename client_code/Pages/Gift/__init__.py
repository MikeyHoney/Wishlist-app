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

@routing.route('Gift', url_keys=['List_Id'], title="Gift")
class Gift(GiftTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.repeating_panel.set_event_handler('x-delete', self.delete_gift)
        #self.List_Id = list_id

    def delete_gift(self, gift, **event_args):
        anvil.server.call('delete_gift', gift)
        self.repeating_panel.items = anvil.server.call('get_gift', list_name=self.List_Name)

    def form_show(self, **event_args):
        url_dict = routing.get_url_dict()

        url_parameters = routing.get_url_hash()
        print(f"URL Parameters: {url_parameters}")
        #list_id = url_parameters
        #list_id = url_parameters.get('List_Id')
        list_id = url_dict.get('List_Id')


      
        if list_id is not None:
            self.List_Id = list_id
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

  #there are 2 servercalls fix
    def add_gift_click(self, **event_args):
        if not self.Name.text:
            alert("You must enter a name!")
            return

        if not self.Description.text:
            alert("You must enter a description!")
            return

        if not self.URL.text:
            alert("You must enter a URL!")
            return

        url_hash = routing.get_url_hash()
        print(f"URL Hash in add_gift_click: {url_hash}")

        list_name = routing.get_url_dict().get('List_Id', None)

        # server call
        list_row = anvil.server.call('get_list_with_gifts', list_id)

        if list_row is not None:
            AddGift = {}
            AddGift['Name'] = self.Name.text
            AddGift['Description'] = self.Description.text
            AddGift['URL'] = self.URL.text
            AddGift['User_Email'] = anvil.users.get_user()['email']

            #server call
            anvil.server.call('add_gift', AddGift, list_id=list_id)
            self.form_show()
        else:
            alert(f"No matching list found for name: {list_id}")