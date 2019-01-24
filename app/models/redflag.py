'''Incidents'''
from datetime import datetime
from db import DataBaseConnection


class Incident():
    '''
    Class with the different methods for manipulating Incident
    '''
    def __init__(self):
        '''Initialising class Incident'''
        dbconn = DataBaseConnection()
        self.cur = dbconn.cur

    def create_redflag(self, redflagtype, location, status, images, videos, comment):
        """Function to register user"""
        redflag_reg = f"""INSERT INTO interventions
        (redflagType, location, status, images, videos, comment)\
        VALUES('{redflagtype}', '{location}', '{status}', '{images}',\
        '{videos}', '{comment}') returning redflagid, created_on, created_by,\
        redflagtype, location, status, images, videos, comment"""
        self.cur.execute(redflag_reg)
        return self.cur.fetchall()

    def get_all_redflag(self):
        """Function to get all redflags from table interventions"""
        get_redflags = f"SELECT * FROM interventions;"
        self.cur.execute(get_redflags)
        redflags = self.cur.fetchall()
        return redflags

    def get_one_redflag(self, redflagId):
        """Function to get one red-flag"""
        get_one_redflag = f"SELECT * FROM interventions where redflagId='{redflagId}';"
        self.cur.execute(get_one_redflag)
        spec_redflags = self.cur.fetchone()
        return spec_redflags

    def update_redflag_location(self, redflagId, location):
        """Function for updating red-flags"""
        update = f"UPDATE interventions SET location ='{location}' WHERE redflagId='{redflagId}' RETURNING redflagId;"
        self.cur.execute(update)
        updated_redflags = self.cur.fetchone()
        return updated_redflags

    def delete_redflag(self, redflagId):
        """Function to delete a red flag"""
        delete_table_q = f"DELETE FROM  interventions where redflagId='{redflagId}';"
        self.cur.execute(delete_table_q)
