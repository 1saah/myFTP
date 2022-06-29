# process different cmd from terminal
# 1. get argv command
# 2. parse cmd
# 3. do as the commands after commands
import os.path





class management_tool(object):

    def __init__(self, argv):
        self.argv = argv
        pass

    def check(self):
        if len(self.argv) < 2:
            help()
            exit()
        cmd = self.argv[1]
        if not hasattr(cmd):
            print('--------valid cmd--------')
            exit()

    def execute(self):
        cmd = self.argv[1]
        func = getattr(cmd)
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
    
    def startserver(self):
        print('--------starting server--------')

    def restartserver(self):
        print('--------restarting server--------')

    def createuser(self):
        print('--------creating user--------')

    def stop(self):
        print('--------stopping server--------')





