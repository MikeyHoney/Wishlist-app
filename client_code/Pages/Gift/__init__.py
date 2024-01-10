from ._anvil_designer import GiftTemplate
#from .NavBar import NavBar  # Import the NavBar custom component
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


from anvil_extras import routing

@routing.route('Gift', url_keys=['List_Name'], title="Gift")
class Gift(GiftTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.repeating_panel.set_event_handler('x-delete', self.delete_gift)
        self.List_Name = None  # Initialize the current_list_name variable

    def delete_gift(self, gift, **event_args):
        anvil.server.call('delete_gift', gift)
        self.repeating_panel.items = anvil.server.call('get_gift', list_name=self.List_Name)

    def form_show(self, **event_args):

        url_parameters = routing.get_url_hash()
        print(f"URL Parameters: {url_parameters}")
        # Retrieve the list name from the URL parameters
        list_name = url_parameters

      
        if list_name is not None:
            self.List_Name = list_name
            gifts = anvil.server.call('get_gift', list_name=list_name)

            if gifts:
                # Proceed with displaying the gifts
                self.repeating_panel.items = gifts
            else:
                # Handle the case where no gifts are found
                self.repeating_panel.items = []  # Clear the repeating panel
                self.add_gift_button.visible = True
                self.no_gifts_label.text = "No gifts have been added to the list."
        else:
            alert("No matching list found in the URL parameters.")
            routing.set_url_hash('')  # Redirect to the home page

    def add_gift_click(self, **event_args):
        if not self.Name.text:
            alert("You must enter a name!")
            return

        if not self.Description.text:
            alert("You must enter a description!")
            return

        if not self.URL.text:
            alert("You must enter a URL!")
            return

        url_hash = routing.get_url_hash()
        print(f"URL Hash in add_gift_click: {url_hash}")

         # Get the list name from the URL parameters
        list_name = routing.get_url_dict().get('List_Name', None)

    # Retrieve the selected list name from the server module
        list_row = anvil.server.call('get_list_name', list_name)

        if list_row is not None:
            AddGift = {}
            AddGift['Name'] = self.Name.text
            AddGift['Description'] = self.Description.text
            AddGift['URL'] = self.URL.text
            AddGift['User_Email'] = anvil.users.get_user()['email']

# Pass the list_name to the server
            anvil.server.call('add_gift', AddGift, list_name=list_name,)
            self.form_show()
        else:
            alert(f"No matching list found for name: {list_name}")