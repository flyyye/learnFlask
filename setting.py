class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'mysql....'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite...'