from run import ma

class NoteSchema(ma.Schema):
  class Meta:
    fields = ('id','title', 'note')