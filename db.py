import psycopg2

class DataBaseConnection:
    """Class to create tables"""
    def __init__(self):
        """Function to initialise class"""
        try:
            self.conn = psycopg2.connect("dbname='ireporter' user='postgres' host='localhost' password='kingsolomon'")
            self.conn.autocommit = True
            self.cur = self.conn.cursor()
            self.create_table()
            print("Connected to the database successfully")
        except (Exception, psycopg2.Error) as error:
            print(error)
    
    def create_table(self):
        """Function to create tables"""
        sql = """CREATE TABLE IF NOT EXISTS user_table
        (userId SERIAL PRIMARY KEY,
        firstname TEXT,
        email TEXT,
        phoneNumber TEXT,
        username TEXT NOT NULL,
        password VARCHAR(10) NOT NULL,
        isAdmin BOOLEAN NOT NULL
        )"""
        self.cur.execute(sql)

        sql1 = """CREATE TABLE IF NOT EXISTS interventions
        (id serial primary key,
        created_on TIMESTAMPTZ DEFAULT Now(),
        created_by SERIAL,
        type text not null,
        location text,
        status text not null,
        images text,
        videos text,
        comment text not null,
        foreign key (created_by)
        REFERENCES user_table(userId)
        )"""
        self.cur.execute(sql1)

    
