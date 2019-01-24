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

    def test_create_incident(self):
        tsql1 = """INSERT INTO interventions 
        (redflagId, created_by, redflagtype, location, status, images, videos, comment)
        VALUES
        (11, 1, 'redflagtype', 'katakwi', 'resolved', 'images', 'videos', 'comment is here'),
        (12, 2, 'redflagtype', 'karuma', 'resolved', 'images2', 'videos2', 'comment is here twice' ),
        (13, 3, 'redflagtype', 'okurut', 'resolved', 'images3', 'videos3', 'comment is here thrice')"""
        self.cur.execute(tsql1)

    def test_create_userdata(self):
        tsql2 = """INSERT INTO user_table
        (userId, name, email, phoneNumber, userName, password, isAdmin)
        VALUES
        (1, 'Kiko', 'pkiko@gmail.com', '0776413515', 'pkiko', '777', 'False' )"""
        self.cur.execute(tsql2)

db = DataBaseConnection() 
