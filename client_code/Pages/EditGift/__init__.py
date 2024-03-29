from ._anvil_designer import EditGiftTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from anvil_extras import routing
@routing.route('EditGift', url_keys=['List_Id', 'Gift_Id'], title='EditGift')
class EditGift(EditGiftTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def form_show(self, **event_args):

      gift = self.fetch_gift_info()
      print(f"{gift}")

      if gift:
        #label_1 = self.label_1 
        #gift['Name']
        #label_1.text = f"gift['Name']"
        self.label_1.text = f"{gift['gift']['Name']}"
        self.label_2.text = f"{gift['gift']['Description']}"
        self.label_3.text = f"{gift['gift']['URL']}"

        #ex
        #label_list = self.label_list
        #label_list.text = f"List Name: {list_info['list_info']['Name']}"
      
        #self.name.text = self.gift['Name']
        #self.description.text = self.gift['Description']
        #self.url.text = self.gift['URL']
      else:
          alert("Failed to retrieve gift information.")

  def save_edit(self, **event_args):
    url_dict = routing.get_url_dict()
    url_parameters = routing.get_url_hash()
    gift_id = self.url_dict.get('Gift_Id')
    
    gift = self.fetch_gift_info()
    updated_data = {}

    if self.Name.text != gift['gift']['Name'] and self.Name.text != '':
        updated_data['Name'] = self.Name.text
    #else:
    #   updated_data['Name'] = gift['gift']['Name']

    if self.Description.text != gift['gift']['Description'] and self.Description.text != '':
        updated_data['Description'] = self.Description.text
    #else:
    #    updated_data['Description'] = gift['gift']['Description']

    if self.URL.text != gift['gift']['URL'] and self.URL.text != '':
        updated_data['URL'] = self.URL.text
    #else:


    if updated_data:
        anvil.server.call('update_gift_details', gift_id, **updated_data)
        alert("Gift updated successfully!")
    #else:


    routing.set_url_hash('List')

  def cancel_edit(self, **event_args):

      alert("The gift edit has been canceled.")
      routing.set_url_hash('List')

  def fetch_gift_info(self):
    url_dict = routing.get_url_dict()
    url_parameters = routing.get_url_hash()
    list_id = self.url_dict.get('List_Id')
    gift_id = self.url_dict.get('Gift_Id')

    ##############
    gift = anvil.server.call('get_gift_info', list_id, gift_id)

    return gift
    
