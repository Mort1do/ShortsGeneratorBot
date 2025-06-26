from sqlalchemy import create_engine

# Подключение к серверу PostgreSQL на localhost с помощью psycopg2 DBAPI
engine = create_engine("postgresql+psycopg2://postgres:Bethelgaze01016@localhost/5433")

engine.connect()

print(engine)