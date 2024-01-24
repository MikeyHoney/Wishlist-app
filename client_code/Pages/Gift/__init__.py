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
        self.repeating_panel.set_event_handler('x-edit', self.edit_gift)

        #self.List_Id = list_id

    def delete_gift(self, gift, **event_args):
        anvil.server.call('delete_gift', gift)
        url_dict = routing.get_url_dict()

        url_parameters = routing.get_url_hash()
        #print(f"URL Parameters: {url_parameters}")
        #list_id = url_parameters
        #list_id = url_parameters.get('List_Id')
        list_id = url_dict.get('List_Id')
        self.repeating_panel.items = anvil.server.call('get_gift', list_id=list_id)

    
    def edit_gift(self, gift, **event_args):
      url_dict = routing.get_url_dict()
      list_id = url_dict.get('List_Id')

      if list_id:
        print(f"Edit Gift - List_Id: {list_id}")

        #gift_id = url_dict.get('gift')
        #gift_id = self.item['Gift_Id']
        gift_id=gift['Gift_Id']
        print(f"Edit Gift - Gift_Id: {gift_id}")

        #edit_gift = anvil.server.call('get_gift_info', list_id, gift_id)
        #print(f"Edit Gift info: {edit_gift}")

        if gift_id:
            routing.set_url_hash(url_pattern='EditGift', url_dict={'List_Id': list_id, 'Gift_Id': gift_id})
        else:
            alert("Failed to edit the gift.")
            routing.set_url_hash('List')
      else:
        alert("List_Id not found in the URL parameters.")
  
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
          
        url_dict = routing.get_url_dict()

        url_parameters = routing.get_url_hash()
        print(f"URL Parameters: {url_parameters}")
        list_id = url_dict.get('List_Id')

        if list_id is None:
          alert("No List_Id found.")
          return
      
        user = anvil.users.get_user('')


        AddGift = {}
        AddGift['Name'] = self.Name.text
        AddGift['Description'] = self.Description.text
        AddGift['URL'] = self.URL.text
        AddGift['User_Email'] = anvil.users.get_user('email')

        new_gift = anvil.server.call('add_gift', AddGift, list_id)
        
        self.form_show()