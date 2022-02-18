#server.py
from simple_websocket_server import WebSocketServer, WebSocket
import json

'''
source : 
https://mandloh.tistory.com/6
'''

class SimpleEcho(WebSocket):
    
    def handle(self):
        print('수신정보' , self.data)
        self.send_message('hihi')
        try:
            json_key = json.loads(self.data)
            
            print('json 수신정보' , self.data)
            print( json_key['move'] )
        except :
            try:
                Move = json.loads(self.data)
                print('move 수신정보' , self.data)
            except:
                print('수신정보' , self.data)
        
        '''
        
        수신했을때 handle 메소드를 타지만
        _handle_packet 이 우선순위가 더 높은것으로 보임.
        _handle_packet이 정의 되어있으면 handle 메소드 무시
        
        
    def _handle_packet(self):
        print(self.address, ' 뭐하는놈인지나 볼까' , self.data)

        '''
        
    def connected(self):
        print(self.address, 'connected')

    def handle_close(self):
        print(self.address, 'closed')

        '''

        send_message(self, 'hi')
        
    
        아주 상세하게 까버림.
        self data 확인해보니 보내주는 데이터 형식같은걸 다까버림
        bytearray(b'a')
        bytearray(b's')
        bytearray(b'd')
        이런형식.
        
    def send_message(self, data):
        self._send_message(False, BINARY, data)
        print(self.address, ' aa 라는걸 보내볼까' , self.data)
        
        '''

    
server = WebSocketServer('localhost', 3000, SimpleEcho)
server.serve_forever()
