from .configs.config import Config
from .lib.authentication import Authentication
from .menu.menu_generator import MenuGenerator
# import typer
from typing import Optional

# app = typer.Typer()

class Application():
    def __init__(self):
        self.configuration = Config(environment="Prod") #TODO: Make this dynamic
        # print(f"running in {self.configuration.get_environment()}")
    
        self.secrets = Authentication()
        # print(f"Credentials are: {self.secrets.get_auth_vars()}")

        # menu = MenuGenerator()
        # menu.paint_menu()
    
