from app import db
from datetime import datetime

class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  titulo = db.Column(db.String(120), nullable=False)
  note = db.Column(db.String(300), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()