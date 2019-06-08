from contextlib import contextmanager
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

connection_url = "mysql+mysqlconnector://root:Zwb@123456@198.12.97.201:3306/test"

engine = create_engine(connection_url, pool_size=5)
Session = sessionmaker(bind=engine)
Base = declarative_base()


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def init():
    Base.metadata.create_all(engine)


class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


if __name__ == "__main__":
        init()
       # session = Session()
        with session_scope() as session:
            user = User(id='11', name='Bob')
            session.add(user)
