class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@host:port/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False