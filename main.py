from models.usuario import Usuario
from database import db

db.create_all()
db.session.commit()

admin = Usuario('nome', 'admin@example.com', 'senha')
guest = Usuario('nome', 'guest@example.com', 'senha')
db.session.add(admin)
db.session.add(guest)
db.session.commit()