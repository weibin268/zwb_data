from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

connection_url = "mysql+mysqlconnector://root:Zwb@123456@198.12.97.201:3306/test"

Base = declarative_base()
engine = create_engine(connection_url)
Session = sessionmaker(bind=engine)


def init():
    Base.metadata.create_all(engine)


class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


if __name__ == "__main__":
        init()
        session = Session()
        user = User(id='1', name='Bob')
        session.add(user)
        session.commit()
        session.close()
