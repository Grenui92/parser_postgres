from connect import Base, engine
from sqlalchemy import String, Column, ForeignKey, Integer, Text, ARRAY
from sqlalchemy.orm import relationship

class Authors(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(250), nullable=False)
    born_date = Column(String(20))
    born_location = Column(String(250))
    description = Column(Text)

class Quote(Base):
    __tablename__ = 'quotes'
    quote_id = Column(Integer, primary_key=True, autoincrement=True)
    tags = Column(ARRAY(Text))
    author = Column(Integer, ForeignKey('authors.author_id', ondelete='CASCADE') )
    quote = Column(Text)
    authors = relationship('Authors', backref='quotes')

if __name__ == '__main__':
    Base.metadata.create_all(engine)