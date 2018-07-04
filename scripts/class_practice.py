from ftplib import FTP
from glob import glob


class Ftp():
    def __init__(self, server=None, user=None, password=None, working_dir=None):
        self.host = server
        self.user = user
        self.password = password
        self.working_dir = working_dir
        #command = "%(self.host)s " % (self.host)
        #command2 = "sh {0}/qscli.sh -P {1} -h {2}".format(self.host, self.password, self.user)
        #print command
        #print command2
    
    def connect(self):
        session = FTP(self.server, self.user, self.password)
        # ftp = FTP('ftp.sunet.se', 'anonymous', 'anonymous@sunet.se')
        raise Exception("Connection Failure")

        return session
    
    def connect_to_ftp(self):
        session = FTP()
        session.connect(self.host, self.port)
        session.login(self.user, self.password)
        return session


    def list_files(self):
        conn = self.connect()
        # conn.retrlines('LIST')
        print str(conn.pwd())
        for filename in glob(str(conn.pwd())+'/'+'*.old'):
            print 'Hey : '+filename

        print "Inside list File of Ftp"
        # print self.server, self.user, self.password, self.working_dir


    def put_file(self):
        session = self.connect()
        f = open('demo.txt', 'rb')
        session.storbinary('STOR demo.txt', f)
        print "File stored"
        f.close()        
        session.quit()
        print "session Quit"



class Sftp():
    def __init__(self, server, user, password, working_dir):
        self.server = server
        self.user = user
        self.password = password
        self.working_dir = working_dir
        
    def list_files(self):
        print "Inside list File  of Sftp"
        print self.server, self.user, self.password, self.working_dir


class EtlFile():
    def __init__(self, protocol, server, user, password, working_dir):
        if protocol == 'ftp':
            print "the protocol is ftp"
            self.protocol_obj = Ftp(server, user, password, working_dir)
        elif protocol == 'sftp':
            print "the protocol is ftp"
            self.protocol_obj = Sftp(server, user, password, working_dir)

        print self.protocol_obj

    def get(self):
        print "Inside get of the EtlFIle"
        #self.protocol_obj.list_files()

    def put(self):
        print "Inside put of the EtlFIle"
        self.protocol_obj.put_file()


def main():
    protocol = 'ftp'
    server = 'ftp.dlptest.com'
    user = 'dlpuser@dlptest.com'
    password = 'hZ3Xr8alJPl8TtE'
    working_dir = ''

    #obj = EtlFile(protocol, server, user, password, working_dir)
    #obj.get()
    # obj.put()
    kwargs = {
            'protocol' : 'ftp',
            'server' : 'ftp.dlptest.com',
            'user' : 'dlpuser@dlptest.com',
            'password' : 'hZ3Xr8alJPl8TtE',
            'working_dir':'',
            }

    obj2 = EtlFile(**kwargs)
    obj2.get()


if __name__ == "__main__":
    main()
