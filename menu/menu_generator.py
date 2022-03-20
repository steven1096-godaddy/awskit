from dataclasses import dataclass
from awskit.menu.menu_item import menu_items
from awskit import __app_name__, __version__


@dataclass
class Menu:
    title: str
    cur_page: str
    prev_page: str
    items: list


class MenuGenerator:
    '''Resposible for orchestrating the Menu Generation process'''
    
    def get_menu_items(self):
        return menu_items
    
    def generate_menu(self):
        menu = Menu(
            "Menu Title Goes Here!",
            None,
            None,
            get_menu_items()
        )
        return menu
        
    def paint_menu(self):
        '''Used for printing the menu to the termninal'''


    

        