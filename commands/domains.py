import typer 

from awskit import current_function # Only for debugging. 
                                    # Remove for production

app = typer.Typer()

@app.command("list")
def list_domains():
    '''
    Display the Route53 hosted domains in the 

    # Example 
    -----
    44.567.123.00 customer-prod-bastion
    52.123.456.78 customer-staging-ec2
    52.321.654.87 customer-dev-ec2
    54.789.654.153 customer-prod-nfs

    '''
    typer.echo(current_function())

@app.command()
def records():
    '''
    Display the records of an individual hosted zone

    Accepts the Hosted Zone ID, or the domain FQD.

    # Example
    -----
    A      mysite.com.              dualstack.mysite-lb-967522168.ap-southeast-1.elb.amazonaws.com.
    A      mysite.com.              11.22.33.44
    TXT    _amazonses.mysite.com.   6c6d761371f0480bbe60de0df275b550
    A      test.mysite.com.         55.66.77.88
    CNAME  www.mysite.com.          mysite.com

    '''
    typer.echo(current_function())

@app.command("clean-zones")
def clean_zones():
    '''
    List or delete any unuzed zones. 
    
    Compares the hosted zones' NS records
    to the public Nameserver records. Shows any hosted zones not in use.

    Accepts the --delete flag to remove the hosted zone.

    # Example. 


    '''
    typer.echo(current_function())
