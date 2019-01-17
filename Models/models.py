from datetime import datetime

class Incident():
    def __init__(self, id, createdOn, createdBy, type, location, status, Images, Videos, comment):
        self.id = id
        self.createdOn = datetime.today()
        self.createdBy = createdBy
        self.type = type
        self.location = location
        self.status = status
        self.Images = Images
        self.Videos = Videos
        self.comment = comment

    def to_json(self):
        return {"id" : self.id, "createdOn" : self.createdOn, "createdBy" : self.createdBy, "type" : self.type, 
        "location" : self.location, "status" : self.status, "Images" : self.Images, "Videos" : self.Videos, 
        "comment": self.comment
        }

