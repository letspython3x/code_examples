import MySQLdb


def execute_query(query):
    conn = MySQLdb.connect(host="localhost",  # your host
                           user="root",  # username
                           passwd="root",  # password
                           db="")
    cursor = conn.curosr()
    return cursor.execute(query)


def show_on_screen(results):
    for r in results:
        print()
        for c in r:
            print(c + '\t')


def save_to_file(results):
    with open('results_file.csv', 'w') as fin:
        header = "geneName\tname\tchrom\tstrand\tcdsStart\tcdsEnd"
        fin.write(header)
        for row in results:
            for col in row:
                fin.write(col + '\t')
            fin.write('\n')


def main():
    query = """select geneName, name, chrom, strand, cdsStart, cdsEnd from refFlat
        where txStarts > 0
        and txEnds <=500000"""

    results = execute_query(query)
    show_on_screen(results)
    print("Records found : ", len(results))
    save_to_file(results)


if __name__ == "__main__":
    main()
