import typer

from awskit import current_function # Only for debugging. 
                                    # Remove for production
                                    
app = typer.Typer()

@app.command("list")
def list_databases():
    '''
    List the Databases and additional useful information
    '''
    typer.echo(current_function())

@app.command()
def metrics():
    '''
    View current & recent database resource usage
    '''
    typer.echo(current_function())

@app.command()
def credentials(
    environment: str = typer.Option("Prod", "--env", "-e",
            help="The environment's database to pull the credentials for")
    ):
    '''
    View the admin user database credentials
    '''
    typer.echo(current_function())
    typer.echo("\nDatabase User: dbadmin\nPassword: Pa22Sdfw0rD\n")


@app.callback()
def callback():
    '''
    Common operations on databases
    '''


if __name__ == "__main__":
    app()