class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'SQLITE:///:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfid(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True