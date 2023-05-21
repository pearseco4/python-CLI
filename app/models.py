from peewee import * 

db = PostgresDatabase('contact_list', user="contact_admin", password='password', host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db
    
class Contact(BaseModel):
    first_name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    email = CharField(max_length=40)

pearse = Contact(first_name='Pearse', last_name='ODonohue', email='pearseco3@gmail.com').save
quinn = Contact(first_name='Quinn', last_name='ODonohue', email='mikaela@gmail.com').save
mikaela = Contact(first_name='Mikaela', last_name='ODonohue', email='quinn@quinn.com').save