# process different cmd from terminal
# 1. get argv command
# 2. parse cmd
# 3. do as the commands after commands
import os.path
from core import server_op




class management_tool(object):

    def __init__(self, argv):
        self.argv = argv
        pass

    def check(self):
        if len(self.argv) < 2:
            help()
            exit()
        cmd = self.argv[1]
        if not hasattr(self, cmd):
            print('--------valid cmd--------')
            exit()

    def execute(self):
        cmd = self.argv[1]
        func = getattr(self, cmd)
        func()

    def help(self):
        print('''
                    --------manage help--------
                    start   ---to start server
                    restart  ---to restart server
                    stop    ---to stop server
                    createuser ---to create new user 
                    help ---to get help menu
        ''')

    def start(self):
        print('--------starting server--------')
        self.server = server_op.Server(self)


    def restart(self):
        print('--------restarting server--------')
        self.server.shutdown()
        self.server.getConn()

    def createuser(self):
        print('--------creating user--------')

    def stop(self):
        print('--------stopping server--------')
        exit()





