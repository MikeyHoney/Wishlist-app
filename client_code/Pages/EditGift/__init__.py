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
@routing.route('EditGift', url_keys=['List_Id'], title='EditGift')
#not sure of routing
class EditGift(EditGiftTemplate):
  def __init__(self, gift, **properties):
    self.init_components(**properties)
    self.gift = gift
    print(f"EditGift - URL Dict: {routing.get_url_dict()}")
    self.name.text = gift['Name']
    self.description.text = gift['Description']
    self.url.text = gift['URL']

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
    