from ._anvil_designer import RowTemplate4Template
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate4(RowTemplate4Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    
    

  def edit_row(self, **event_args):
    #anvil.server.call('open_edit_form', list_id=self.item['List_Id'])\
    #gift_id = self.item['Gift_Id']
    self.parent.raise_event('x-edit', gift=self.item)


  def delete_row_click(self, **event_args):
    self.parent.raise_event('x-delete', gift=self.item)




 




