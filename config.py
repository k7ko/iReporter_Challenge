class Config(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'SQLITE:///:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://ireporter@localhost/foo'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True