import optparse

class Client(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-p", "--port", type="int", dest="port", help="port")
        parser.add_option("-s", "--server", dest="server", help="server")
        parser.add_option("-u", "--username", dest="username", help="username")
        parser.add_option("-w", "--password", dest="password", help="password")
        self.options, self.args = parser.parse_args()
        print(self.options, self.args)

if __name__ == "__main__":
    client = Client()