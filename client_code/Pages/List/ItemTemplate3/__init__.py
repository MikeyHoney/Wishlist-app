from ._anvil_designer import ItemTemplate3Template
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing



class ItemTemplate3(ItemTemplate3Template):
  def __init__(self, **properties):

    self.init_components(**properties)


  def list_link_click(self, **event_args):

    name = self.list_link.text
    print(f"This is the name of the list: {name}")



    self.open_gift_page(name)
    
  def open_gift_page(self, name):

    #routing.set_url_hash(url_pattern='Gift', url_dict={'Name': self.item['Name']})

    routing.set_url_hash(url_pattern='Gift', url_dict={'List_Name': self.item['Name']})

  
    #url_pattern='article', url_dict={'id':self.item['id']}


    
  pass


  

