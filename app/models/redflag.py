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

    def create_redflag(self, redflagType, location, status, images, videos, comment):
        """Function to register user"""
        redflag_reg = f"""INSERT INTO user_table
        (redflagType, location, status, images, videos, comment) VALUES ('{redflagType}', '{location}', '{status}', '{images}', '{videos}', '{comment}')"""
        self.cur.execute(redflag_reg)

    def get_all_redflag(self, username):
        """Function to get all redflags from table interventions"""
        get_redflags = f"SELECT * FROM interventions;"
        self.cur.execute(get_redflags)
        redflags = self.cur.fetchone()
        return redflags

    def get_one_redflag(self):
        """Function to get one red-flag"""
        get_one_redflag = f"SELECT * FROM interventions where redflagId='{redflagId}';"
        self.cur.execute(get_one_redflag)
        spec_redflags = self.cur.fetchone()
        return spec_redflags

    def update_redflag(self):
        """Function for updating red-flags"""
        update = f"UPDATE interventions WHERE redflagId='{redflagId}';"
        self.cur.execute(update)
        updated_redflags = self.cur.fetchone()
        return updated_redflags

    def delete_table(self):
        """Function to delete a table"""
        delete_table_q = f"""DROP TABLE user_table"""
        self.cur.execute(delete_table_q)

