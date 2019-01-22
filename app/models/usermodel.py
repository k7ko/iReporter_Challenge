'''User'''
from db import DataBaseConnection

class User():
    '''
    Class with the different methods for manipulating user
    '''
    def __init__(self):
        '''Initialising class user'''
        dbconn = DataBaseConnection()
        self.cur = dbconn.cur

    def register_user(self, username, password):
        """Function to register user"""
        user_reg = f"""INSERT INTO user_table
        (username, password) VALUES ('{username}', '{password}')"""
        self.cur.execute(user_reg)

    def check_user_name(self, username):
        """Function to check if username already exists"""
        user_check_q = """SELECT * FROM user_table where username='{username}'"""
        self.cur.execute(user_check_q)
        user_check = self.cur.fetchone()
        return user_check

    def login_user(self,username):
        """Function to log in user"""
        user_login = f"""SELECT * FROM user_table where username='{username}'""" 
        self.cur.execute(user_login)
        user = self.cur.fetchone()
        return user

    def delete_table(self):
        """Function to delete a table"""
        delete_table_q = f"""DROP TABLE user_table"""
        self.cur.execute(delete_table_q)

