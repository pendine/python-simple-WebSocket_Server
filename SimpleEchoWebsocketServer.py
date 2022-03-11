from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class SimpleEcho(WebSocket):

    def handleMessage(self):
    # echo message back to client
        self.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleEcho('', 9888, SimpleEcho)
server.serveforever()
