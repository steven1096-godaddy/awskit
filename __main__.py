from awskit import __app_name__, __version__
from typing import Optional
import typer


from awskit.commands import (
    investigate, 
    databases, 
    domains, 
    servers,
    ssl,
    keys
)
# from awskit.lib.common import eval_expression, add_command


app = typer.Typer(add_completion=False)

def version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.command()
def menu(): #(menu_select: Menu = typer.Option(None)):
    '''Start Awskit in menu mode'''
    typer.echo("Starting Menu")


@app.callback(invoke_without_command=True)
def callback(
    version: Optional[bool] = typer.Option(
            None, "--version", callback=version_callback, is_eager=True,
            help=f"Displays the Version Number of the {__app_name__}"
        ),
    ):
    '''The AWS Kit Framework - For Use by Technical Services Cloud Team'''
    pass

app.add_typer(investigate.app, name="investigate")
app.add_typer(databases.app, name="databases")
app.add_typer(domains.app, name="domains")
app.add_typer(servers.app, name="servers")
app.add_typer(ssl.app, name="ssl")
app.add_typer(keys.app, name="keys")



if __name__ == "__main__":
    app()
    


# END


# @app.callback()
# def main(verbose: bool = True,
#          version: bool = typer.Option(
#             None, "--version", 
#             callback=version_callback, 
#             is_eager=True),
# #         ):
#     """
#     AWS Kit

#     Command Line Tool for managing Technical Services - AWS Cloud Infrastructure\n
#     """
    # if verbose:
    #     typer.echo("Will write verbose output")
    #     state["verbose"] = True

# @app.command()
# def hello(name: str):
#     typer.echo(f"Hello {name}")

# @app.command()
# def goodbye(name: str, formal: bool = False):
#     if formal:
#         typer.echo(f"Goodbye Ms. {name}. Have a good day.")
#     else:
#         typer.echo(f"Bye {name}!")

# def main(name: str):
#     # app()
#     typer.echo((f"Hello {name} {__app_name__} v{__version__}"))



# def main(
#     name: str,
#     password: str = typer.Option(
#         ..., prompt=True, confirmation_prompt=True, hide_input=True
#     ),
# ):
#     typer.echo(f"Hello {name}. Doing something very secure with password.")
#     typer.echo(f"...just kidding, here it is, very insecure: {password}")



# def main(menu: Optional[str] = typer.Argument(False, help="Start Awskit in menu mode."),
#          database: Optional[bool] = typer.Argument(False, help="Common operations on database"),
#          servers: Optional[bool] = typer.Argument(False, help="Common server & auto scaling operations"),
#          domains: Optional[bool] = typer.Argument(False, help="Common operations on domains R Route53"),
#          investigate: Optional[bool]  = typer.Argument(False, help="Userful troubleshooting operations"),
#          verbose: bool = False):
#     """
#     Usage:
#     $ awskit <service> <option>
 

#     If --verbose is used, display debug output.
#     """
#     if selection is None:
#         no_selection()
    
#     message_start = "everything is "
#     if good:
#         ending = typer.style("good")
#     else:
#         ending = typer.style("bad")
#     message = message_start + ending
#     typer.echo(message)
#     # if formal:
#     #     typer.echo(f"Good day Ms. {name} {lastname}.")
#     # else:
#     #     typer.echo(f"Hello {name} {lastname}")





    # database: Optional[bool] = typer.Argument(False, help="Common operations on database"),
#          servers: Optional[bool] = typer.Argument(False, help="Common server & auto scaling operations"),
#          domains: Optional[bool] = typer.Argument(False, help="Common operations on domains R Route53"),
#          investigate: Optional[bool]  = typer.Argument(False, help="Userful troubleshooting operations"),
#          verbose: bool = False):


# @app.command()
# def databases(db: Optional[str] = typer.Argument(False, help="The database to act on")):
#     '''Common operations on databases'''
#     typer.echo("Calling the database AWSKit command")



