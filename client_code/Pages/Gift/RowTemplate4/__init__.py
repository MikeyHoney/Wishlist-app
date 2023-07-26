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
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def edit_row(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def delete_row(self, **event_args):
    # Get the unique identifier of the gift row to be deleted (e.g., 'gift_id')
    gift_name = self.item['Name']  # Assuming 'GiftId' is the column name for the unique identifier

    # Call the server function to delete the gift row by its ID
    anvil.server.call('delete_gift', gift_name)

    # Remove the item from the repeating panel
    self.remove_from_parent()



