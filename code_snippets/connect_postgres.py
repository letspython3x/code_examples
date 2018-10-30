import random
import string
import psycopg2 as db


def id_generator(size=6):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


def write_to_csv(fname):
    print("Creating csv with random name & id")
    with open(fname, 'w') as fin:
        count = 2
        while count < 12:
            line = id_generator(5)
            fin.write(line + ',' + str(count) + '\n')
            count += 1


def load_csv_to_db(fname):
    print("Laoding file to database")
    try:
        conn = db.connect(host='localhost', database="testdb", user="postgres", password="postgres")

        cur = conn.cursor()
        with open(fname) as fout:
            for line in fout:
                name, id = line.split(',')
                query = "INSERT INTO test_table_1 VALUES ('{}', '{}');".format(name, id)
                cur.execute(query)
                print("file loaded")
    except (Exception, db.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def connect_db():
    conn = db.connect(host="127.0.0.1", port="5432", database="testdb", user="postgres", password="postgres")
    print("Opened database successfully")
    cur = conn.cursor()

    query = "INSERT INTO test_table_1 VALUES ('Akshay', '3');"
    cur.execute(query)
    conn.commit()

    query = "select name from test_table_1;"
    r = cur.execute(query)
    conn.rollback()
    print(query)
    print("Query results: ", r.fetchall())
    conn.close()


def run():
    fname = 'load_data.csv'
    # write_to_csv(fname)
    # load_csv_to_db(fname)
    connect_db()


if __name__ == "__main__":
    run()
