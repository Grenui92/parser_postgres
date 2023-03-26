from configparser import ConfigParser

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from datetime import datetime



config = ConfigParser()
config.read('config.ini')
user_name = config.get('DB', 'user')
password = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
host = config.get('DB', 'host')
port = config.get('DB', 'port')


engine = create_engine(f'postgresql+psycopg2://{user_name}:{password}@{host}:{port}/{db_name}')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


