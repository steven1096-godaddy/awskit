import typer

from awskit import current_function # Only for debugging. 

app = typer.Typer()


@app.command("list")
def list_servers():
    '''
    List Availible Servers and their public IPs
    '''
    typer.echo(current_function())

@app.command()
def command():
    '''
    Run a command on a single or all instances of an ASG
    '''
    typer.echo(current_function())

@app.callback()
def callback():
    '''
    Common operations on servers/EC2 Instances
    '''

if __name__ == "__main__":
    app()