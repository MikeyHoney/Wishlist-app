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

    list_id = self.url_dict.get('List_Id')
    gift_id = self.url_dict.get('Gift_Id')

    if list_id and gift_id:
      self.gift = anvil.server.call('get_gift_info', list_id, gift_id)

      if self.gift:
        self.name.text = self.gift['Name']
        self.description.text = self.gift['Description']
        self.url.text = self.gift['URL']
      else:
          alert("Failed to retrieve gift information.")
          self.close()
    else:
      alert("List_Id or Gift_Id not found in the URL parameters.")
      self.close()

  def save_edit(self, **event_args):
    updated_data = {}

    if self.name_textbox.text != self.gift['Name']:
      updated_data['Name'] = self.name_textbox.text

    if self.description_textbox.text != self.gift['Description']:
      updated_data['Description'] = self.description_textbox.text

    if self.url_textbox.text != self.gift['URL']:
      updated_data['URL'] = self.url_textbox.text

    if updated_data:
      anvil.server.call('update_gift_details', self.gift['Gift_Id'], list_id, **updated_data)

    self.close()

  def cancel_edit(self, **event_args):
      self.close()
    