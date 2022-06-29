import socket
from core import management
# 传输文件（服务器方）
# 传输文件需要首先用结构体打包文件头信息的大小传输过去，由于装文件头大小的数据是integer，大小是固定的，所以接收方统一用recv（4）来接收，结构体需要编码成utf-8 或者 GBK
# 之后需要传输文件头。文件头包含了要传输文件的各种信息，他是本体是一个键值对的dictionary，需要用json.dumps()和json.loads()从dictionary和string之间来回转换，之后在再在string和utf-8和gbk之间转换
# 最后则是根据打开文件的大小来一行一行传输文件（避免单次过大爆内存）
#
# 粘包现象
# 如若某次信息未接收完，信息会堵塞在传输管道，在下一次接受信息时会优先拿到上次未接收完的信息
# 解决方法：提前得知文件大小！根据文件大小来循环接受，直到完全接受整个文件包，类似上面的传输文件。
#
# FTP目的分析：根据控制台输入的命令来执行结果， 所以并不需要文件的传输，主要是账户命令的指令，所以只要反馈给用户一些执行成功的信息就可以了。
# 那么在这个地方我们仅仅需要连接到客户端，不停地执行命令即可。
# 本地接受terminal命令
#
#
from conf import setting

class Server:
    def __init__(self, management_tool):
        self.management_tool = management_tool
        pass

    def createSocket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(setting.IP, setting.PORT)
        self.server_socket.listen(setting.MAX_LISTEN)

    def getConn(self):
        self.conn, self.addr = self.server_socket.accept()
        pass

    def runForever(self):
        pass

    def shutdown(self):
        if not self.conn:
            exit()
        else:
            self.conn.close()


