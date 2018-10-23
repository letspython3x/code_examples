import csv
def csv_update(filepath):
    with open(filepath+'/csv.csv', 'rb') as fin:
        keys = fin.readline().split(',')
        for line in fin.readlines():
            print ("Line: %s"%line)
            line = line.strip('/n')
            keys[0] = line.split(',')[0]
            values = line.split(',')
            for pos,val in enumerate(values):
                print ("{}:{}".format(keys[pos], values[pos]))

def use_csv_module(filepath):
    fout = open(filepath+'output.csv', 'wb')
    with open(filepath + 'csv.csv', 'rb') as fin:
        file_reader = csv.reader(fin, delimiter=',')
        keys = list()
        for pos, line in enumerate(file_reader):
            # Read 1st line to get the header (keys)
            if pos==0:
                keys = line
                print (keys)
                continue
            else:
                # pick the date
                keys[0] = line[0]
                # field Values
                values = line[0:]
            for pos in range(1,len(line)):
                writer = csv.writer(fout)
                iterable = "{} -{}:{}".format(keys[0],keys[pos], values[pos]).split(',')
                writer.writerows(iterable)
                #print ("{} -{}:{}".formast(keys[0],keys[pos], values[pos]))
        fout.close()


def main():
    filepath = r"/home/ab.gupta/test//"
    #csv_update(filepath)
    use_csv_module(filepath)

if __name__ == "__main__":
    main()