import typer 

from awskit import current_function # Only for debugging. 


app = typer.Typer()

@app.command("list")
def list_ssl_certificates():
    '''
    List all SSL certificates in the primary zone or zone passed in 
    as an option.'''
    typer.echo(current_function())

@app.command("import")
def import_ssl():
    '''
    Imports a provided 3rd party CA-CRT into ACM. 
    
    Accepts the private key, certificate, certificate chains, & region
    as options. Valid options include absolute & relative path. 

    This operation will check for an existing ACM in the primary region, or 
    the region passed in as an option. It will then import the new CRT into ACM and
    return the ARN. 
    '''

@app.callback()
def callback():
    '''
    Common operations on SSL & ACM certificates
    '''

if __name__ == "__main__":
    app()
