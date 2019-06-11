from contextlib import contextmanager
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import collections
import sqlalchemy.engine.result

class DbClient:

    def __init__(self, *args, **kwargs):
        self.engine = create_engine(*args, **kwargs)
        self.Session = sessionmaker(bind=self.engine)
        self.Base = declarative_base()

    def open_session(self):
        return self.Session()

    @contextmanager
    def open_session_scope(self):
        session = self.open_session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def init(self):
        self.Base.metadata.create_all(engine)


def result_to_namedtuple(result: sqlalchemy.engine.result.ResultProxy):
    Record = collections.namedtuple('Record', result.keys())
    records = [Record(*r) for r in result.fetchall()]
    return records


if __name__ == "__main__":
    db = DbClient("mysql+mysqlconnector://root:root@192.168.19.11/demo")

    class User(db.Base):
        __tablename__ = 'user'
        id = Column(String(20), primary_key=True)
        name = Column(String(20))

    with db.open_session_scope() as session:
        records= result_to_namedtuple( session.execute("select * from user"))
        for r in records:
            print(r.id)
