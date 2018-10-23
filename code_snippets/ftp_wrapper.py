from ftplib import FTP
from glob import glob


class Ftp():
    def __init__(self, server=None, user=None, password=None, working_dir=None):
        self.host = server
        self.user = user
        self.password = password
        self.working_dir = working_dir

    def connect(self):
        try:
            session = FTP(self.host, self.user, self.password)
            # ftp = FTP('ftp.sunet.se', 'anonymous', 'anonymous@sunet.se')
            return session
        except:
            raise Exception("Connection Failure")

    def connect_to_ftp(self):
        session = FTP()
        session.connect(self.host, self.port)
        session.login(self.user, self.password)
        return session

    def list_files(self):
        conn = self.connect()
        # conn.retrlines('LIST')
        print(str(conn.pwd()))
        for filename in glob(str(conn.pwd()) + '/' + '*.old'):
            print('Hey : ' + filename)

        print("Inside list File of Ftp")
        print(self.host, self.user, self.password, self.working_dir)

    def put_file(self):
        session = self.connect()
        f = open('demo.txt', 'rb')
        session.storbinary('STOR demo.txt', f)
        print("File Uploaded")
        f.close()
        session.quit()
        print("session Quit")


def main():
    kwargs = {
        'protocol': 'ftp',
        'server': 'ftp.dlptest.com',
        'user': 'dlpuser@dlptest.com',
        'password': 'hZ3Xr8alJPl8TtE',
        'working_dir': '',
    }

    obj2 = Ftp(**kwargs)


if __name__ == "__main__":
    main()
