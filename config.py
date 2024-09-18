class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:12345678@localhost:5432/usermanagement'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
