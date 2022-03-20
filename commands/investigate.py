import typer
from typing import Optional
from datetime import datetime

from awskit.lib import common

from awskit import current_function

app = typer.Typer()


class Investigator():
    def __init__(self, t):
        '''
        The Investigator class houses the functions that do the 
        actual work of querying the AWS infrastructure

        Usefull when investigating alarms or outages.
        '''
        self.current_utc = t["utc_time"]
        self.current_local = t["local_time"]
    
    @classmethod
    def list_databases(cls, region):
        '''List the RDS instances in the default region.'''
        typer.echo(f"Listing RDS databases in {region}")
        typer.echo(3*"rds-1    FQDN\n")

    def get_running_queries(self, database, region):
        typer.echo(f"{current_function()} with {database} in {region}")





@app.command()
def traffic():
    '''
    Print the access logs to a particular ASG
    
    Output based on parameters provided - like start and end time.
    '''
    typer.echo("Calling the investigate traffic command")


@app.command()
def database_queries(
        database: Optional[str] = typer.Option(
                    None, "--database", "-d",
                    help="The database to investigate"),
        region: Optional[str] = typer.Option(
                    common.get_default_region(), "--region", "-r",
                    help="The region to operate in. Only needed " \
                    "if different than the default region on the account")
    ):
    '''
    Investigate Database issues.

    Useful for viewing current running queries, listing variables, etc.
    '''
    if database is None:
        Investigator.list_databases(region)
        typer.echo("Select a database to view running queries")
        database = input()

    investigator_app = Investigator(common.get_timestamps())
    investigator_app.get_running_queries(database, region)




@app.command()
def resources():
    '''
    View Resource Usage data
    '''
    typer.echo("Gathering Resuource Usage Metrics")



@app.callback()
def callback():
    '''
    Useful Investigation Operations

    Userfull for investigating the traffic from access logs or viewing metric resource information

    Use this to speed up your troubleshooting & investigative efforts.
    '''
    pass

if __name__ == "__main__":
    app()