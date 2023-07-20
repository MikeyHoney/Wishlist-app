from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
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

  def home_link(self, **event_args):
    routing.set_url_hash('')

  def update_links(self):
    user = anvil.users.get_user()
    self.HomeLink.visible = bool(user)
    self.ListLink.visible = bool(user)
    self.LoginLink.visible = bool(not user)
    #self.logout_link_click.visible = bool(user)

  def list_link(self, **event_args):
    routing.set_url_hash('List')

  def login_link(self, **event_args):
    anvil.users.login_with_form(allow_cancel=True)
    anvil.users.signup_with_form()

    self.update_links()
    routing.set_url_hash('Login')

  #anvil.users.signup_with_form()

    
  def logout(self, **event_args):
    anvil.users.logout()
    self.update_links()
    routing.set_url_hash('')
    routing.clear_cache()

  def login(self, **event_args):
    anvil.users.login_with_form(allow_cancel=True)
    self.update_links()
    routing.set_url_hash('')

  def form_show(self, **event_args):
    if not anvil.users.get_user():
      routing.set_url_hash('Login')
      alert('You must be logged in to add to / create a list')

 
