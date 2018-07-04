import os


class Base(object):
    def __init__(self, **kwargs):
        self.host = kwargs['host']


class FileAcquisition:
    def __init__(self, host, protocol, username=None):
        #super(FileAcquisition, self).__init__(**kwargs)
        self.protocol = protocol
        self.username = username
        self.host = host
        #FileAcquisition.protocol = var1


    def print_var(self):
        print self.protocol
        print self.username
        print self.host
        #print FileAcquisition.protocol
    
    def change_class_var(self):
        FileAcquisition.protocol = 'I am changed'

    def execute(self):
        args = {
                'user':'test_user'
                }
        command = "sh test_bash.sh --username %(user)s" % (args)
        # r = os.popen('sh test_bash.sh --username user').read()
        r=os.popen(command).read()
        print command
        print (r)
        print type(r)
       



val = { 'host':'test_host',
        
        'protocol' : 'ftp'
        
        }


val2 = {
        'protocol':'SftpOperations',
        'username': 'Sftp user',
        'host':'sftp_host'

        }

var1 = 'from out'
obj = FileAcquisition(**val)
obj.print_var()

#FileAcquisition.protocol= 'Protocol Out'

#obj1 = FileAcquisition(var1, **val2)
#obj1.print_var()
#obj1.change_class_var()
#obj1.print_var()
#obj.print_var()

#obj.execute()
