import psycopg2
from psycopg2.extras import RealDictCursor


class DataBaseConnection:
    """Class to create tables"""
    def __init__(self):
        """Function to initialise class"""
        try:
            self.conn = psycopg2.connect("dbname='ireporter' user='postgres' host='localhost' password='kingsolomon'")
            self.conn.autocommit = True
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
            self.create_table()
            print("Connected to the database successfully")
        except (Exception, psycopg2.Error) as error:
            print(error)

    def create_table(self):
        """Function to create tables"""
        sql = """CREATE TABLE IF NOT EXISTS user_table
        (userId SERIAL PRIMARY KEY,
        name TEXT,
        email TEXT,
        phoneNumber TEXT,
        username VARCHAR(17) NOT NULL,
        password VARCHAR(255) NOT NULL,
        isAdmin BOOLEAN NOT NULL
        )"""
        self.cur.execute(sql)

        sql1 = """CREATE TABLE IF NOT EXISTS interventions
        (redflagId serial primary key,
        created_on TIMESTAMPTZ DEFAULT Now(),
        created_by SERIAL,
        redflagtype VARCHAR(15) NOT NULL,
        location VARCHAR(25),
        status text NOT NULL,
        images text,
        videos text,
        comment VARCHAR(500) NOT NULL,
        foreign key (created_by)
        REFERENCES user_table(userId)
        )"""
        self.cur.execute(sql1)

db = DataBaseConnection() 
