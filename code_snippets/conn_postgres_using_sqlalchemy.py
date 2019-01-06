from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session

conn_string = 'postgresql://{user}:{password}@{hostname}/{database}'.format(database='testdb', user='postgres',
                                                                                     password='postgres',
                                                                                     hostname='127.0.0.1')



conn_string = 'postgresql://{user}:{password}@{hostname}/{database}'.format(database='shuttl', user='kong',
                                                                                     password='kong',
                                                                                     hostname='10.111.179.165')


engine = create_engine(conn_string)
Session = scoped_session(sessionmaker(bind=engine))
s = Session()

params = {'name': 'Karan'}
sql = text("""SELECT * FROM test_table_1 WHERE name = :name""")
sql = text("""SELECT * FROM test_table_1""")

sql = text("""SELECT * FROM conductor""")
# query = """INSERT INTO test_table_1 VALUES ('Prakhar', '4');"""
result = s.execute(sql, params)
# s.execute("""COMMIT""")
s.commit()
print(result.fetchall())
print("data inserted")
s.close()
