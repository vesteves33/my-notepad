from app import db
from datetime import datetime

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(30), nullable=False)
  sobrenome = db.Column(db.String(80))
  email = db.Column(db.String(120), unique=True, nullable=False)
  senha = db.Column(db.String(12), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self) -> str:
    return f"<User {self.nome}>"

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
