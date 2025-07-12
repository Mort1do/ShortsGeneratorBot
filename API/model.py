from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import UUID
import uuid


# Подключение к серверу PostgreSQL на localhost с помощью psycopg2 DBAPI
engine = create_engine("postgresql+psycopg2://postgres:Bethelgaze01016@localhost:5433/test1")
engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print(engine)
print(type(SessionLocal))

Base = declarative_base()

class Accounts(Base):
    __tablename__ = "accounts"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    email_password = Column(String, nullable=False)
    description = Column(String)


# ORM using DB
def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def getAllAcc():
    with getDb() as db:
        accounts = db.query(Accounts).all()
    return accounts

def getAccByNum(position):
    with SessionLocal() as db:
        account = db.query(Accounts).order_by(Accounts.id).offset(position).limit(1).first()
    return account

def getAccByLogin(login):
    with getDb() as db:
        account = db.query(Accounts).filter(Accounts.login == login).first()
    return account

def putAcc(login, password, email, emailPassword, description=""):
    with getDb() as db:
        newAcc = Accounts(login=login, password=password, email=email, email_password=emailPassword, description=description)
        try:
            db.add(newAcc)
            db.commit()
            return True
        except:
            print("Can't INSERT new element")
            return False


#new_account = Accounts(login="test1", password="test1", email="test1", email_password="test1")
#db.add(new_account)
#db.commit()

# SELECT (получение всех записей)
#accounts = db.query(Accounts).all()
#for acc in accounts:
#    print(acc.login, acc.email)

#db.close()