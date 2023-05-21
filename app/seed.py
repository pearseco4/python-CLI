from models import db, Contact

db.drop_tables([Contact])
db.create_tables([Contact])