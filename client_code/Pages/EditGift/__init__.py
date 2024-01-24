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
    url_dict = routing.get_url_dict()

    url_parameters = routing.get_url_hash()
    list_id = self.url_dict.get('List_Id')
    gift_id = self.url_dict.get('Gift_Id')

    if list_id and gift_id:
      #print(f"Gift Object: {self.gift}")  # Add this line to inspect the 'gift' object

      gift = anvil.server.call('get_gift_info', list_id, gift_id)
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
          self.close()
    else:
      alert("List_Id or Gift_Id not found in the URL parameters.")
      self.close()

  def save_edit(self, **event_args):
    updated_data = {}

    if self.Name.text != gift['Name']:
      updated_data['Name'] = self.name_textbox.text

    if self.Description.text != self.gift['Description']:
      updated_data['Description'] = self.description_textbox.text

    if self.URL.text != self.gift['URL']:
      updated_data['URL'] = self.url_textbox.text

    if updated_data:
      anvil.server.call('update_gift_details', self.gift['Gift_Id'], list_id, **updated_data)

    self.close()

  def cancel_edit(self, **event_args):
      self.close()
