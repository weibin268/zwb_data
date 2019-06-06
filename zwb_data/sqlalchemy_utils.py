from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

default_session_key = "default_session_key"
default_session_connection_string = "mysql+mysqlconnector://root:root@192.168.19.11:3306/demo"

dict_sessionmaker = {}


def get_sessionmaker(*args, **kwargs):

    dict_sessionmaker.get(default_session_connection_string)
    engine = create_engine(*args, **kwargs)


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))


Base.metadata.create_all(engine)

# 创建DBSession类型:
Session = sessionmaker(bind=engine)
print(type(Session))
session = Session()
print(type(session))
user = User(id='5', name='Bob')
# 添加到session:
session.add(user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
