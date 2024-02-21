from bson import ObjectId
import datetime


class Note:
    id_Note = 0

    def __init__(self,title,created_date,is_done,content):
        Note.id_Note += 1

        self.objectID_note = ObjectId(str(Note.id_Note))
        self.title = title
        self.created_date = str(datetime.date)
        self.is_done = is_done
        self.content = content
    
    def to_json(self):
        return{
            'id_note': str(self.objectID_note),
            'title': self.title,
            'created_date': str(self.created_date),
            'is_done': self.is_done,
            'content': self.content
        }