from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.tables as tables 
import anvil.tables.query as q
from anvil.tables import app_tables

from anvil_extras import routing

from ..Pages.Home import Home
from ..Pages.List import List
from ..Pages.Login import Login

@routing.main_router
class HomeForm(HomeFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def HomeLink(self, **event_args):
    routing.set_url_hash('')
    pass

  def ListLink(self, **event_args):
    routing.set_url_hash('List')
    pass

  def LoginLink(self, **event_args):
    routing.set_url_hash('Login')
    pass






