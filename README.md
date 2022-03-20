# AWS Kit - Infrastrucrure Manager CLI

#### A project to help manage the AWS Infrastructure

This is a project put together to help manage AWS infrastructure, and hopefully abstract much of the complexity of managing it. 

It relies heavily on convention over confifguration, leaning on the most common services requested and performed. 

## How to use

### Clone the repository
```bash
user@host ~ $ git clone git@github.com:steven1096-godaddy/awskit.git

```

### Create a Symbolic soft link, in your infrastructure's root directory
```bash
user@host ~ $ cd /path/to/infra/root && ln -s /path/to/awskit

```

### Run as a module | Some Examples
```bash
user@host ~ $ python3 -m awskit --help

user@host ~ $ python3 -m awskit domains list

user@host ~ $ python3 -m awskit investigate database-queries -d {database} - r {region}

```


