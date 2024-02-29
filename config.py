
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '386d859545e57f7bf41cb5abc1ed8af68bb715ec5529b42fb3063ad1931eb959'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
