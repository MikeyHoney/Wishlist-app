from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
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
    self.update_links()

    # Any code you write here will run before the form opens.

 # def update_links(self):
  #  user = anvil.users.get_user()
  #  self.add_task_link.visible = bool(user)
    

  def home_link_click(self, **event_args):
    routing.set_url_hash('')
    pass

  def list_link_click(self, **event_args):
    routing.set_url_hash('List')
    pass

  def login_link_click(self, **event_args):
    routing.set_url_hash('Login')
    pass

  def form_show(self, **event_args):
    if not anvil.users.get_user():
      routing.set_url_hash('Login')
      alert('You must be logged in to add to / create a list')