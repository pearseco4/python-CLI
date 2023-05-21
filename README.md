# python-CLI

## contact list comand list application

## Installation 
1. Clone this repository
2. Install required dependencies

## To run this application, navigate to the project directory and execute the main.py script

### ```-c```, ```--create``` will create a new contact. This requires three arguments: first_name, last_name, and email.

### ```-l```, ```--list``` will list all contacts.
### -f, --find will find a contact by their first name. This requires the first_name argument.

## Ex. 


### Create a new contact
``--create Pearse ODonohue pearseco@gmail.com``

### Find a contact by first name
```--find Pearse```

### Database 
This app uses a SQLite database to store contacts. The database file is located at `database/contacts.db`. The tables are created automatically when you run the seed script.

### Seed Script 
To create databases and tables, use the seed scipt seed.py. Run the following command:

`something`




