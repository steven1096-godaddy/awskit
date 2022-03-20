import typer

from awskit import current_function # Only for debugging

app = typer.Typer()

@app.command("list")
def list_ssm_parameters():
    '''
    List all available SSM parameters in the default region or the region
    passed in as an option.
    '''
    typer.echo(current_function())

@app.command()
def search():
    '''
    Searches for and returns a list of SSM parameters that include a 
    string passed in as an argument.
    '''
    typer.echo(current_function())

@app.callback()
def callback():
    '''
    Common operations on SSM Parameters & Parameter Store
    '''
    pass