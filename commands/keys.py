import typer 

from awskit import current_function # Only for debugging. 


app = typer.Typer()

@app.command("list")
def list_ssh_keys():
    '''
    List all SSL certificates in the primary zone or zone passed in 
    as an option.'''
    typer.echo(current_function())

@app.command()
def deploy():
    '''
    Deploys SSH keys to an all SSH key buckets. 
    
    Accepts a list of buckets as an option.
    '''


@app.callback()
def callback():
    '''
    Common operations on SSH Keys
    '''
    pass

if __name__ == "__main__":
    app()
