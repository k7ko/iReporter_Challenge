'''Incidents'''
from datetime import datetime

class Incident():
    '''
    Class describing Incident
    '''
    def __init__(self, id, created_on, created_by, type, location, status, images, videos, comment):
        '''Initialing attributes of class'''
        self.id = id
        self.created_on = datetime.today()
        self.created_by = created_by
        self.type = type
        self.location = location
        self.status = status
        self.images = images
        self.videos = videos
        self.comment = comment

    def to_json(self):
        '''converting to json'''
        return {
            "id" : self.id,
            "created_on" : self.created_on,
            "created_by" : self.created_by,
            "type" : self.type,
            "location" : self.location,
            "status" : self.status,
            "images" : self.images,
            "videos" : self.videos,
            "comment": self.comment
        }
