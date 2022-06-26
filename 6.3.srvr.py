import socket
import sys
import time
import errno
import math #import math library to perform calculation function like LOG, SQUARE ROOT etc
from multiprocessing import Process

ok_message = '\nHTTP/1.0 200 OK\n\n'
nok_message = '\nHTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode("Python Calculator (LOG <log>, SQUARE ROOT <sqrt>, EXPONENTIAL <exp>)\n =================================== \n Instruction: log/sqrt/exp <number>\n Example: log >: log 10\n =================================== \n \t\tType 'exit' to close"))
    while True:
        data = s_sock.recv(2048) #input from client
        data = data.decode("utf-8")

        #calculation
        try:
            operation, value = data.split()
            op = str(operation)
            num = int(value)

            if op[0] == 'l':
                op = 'Log'
                answer = math.log10(num)
            elif op[0] == 's':
                op = 'Square root'
                answer = math.sqrt(num)
            elif op[0] == 'e':
                op = 'Exponential'
                answer = math.exp(num)
            else:
                answer = ('ERROR!')

            sendAnswer = (str(op) + '(' + str(num) + ') = ' + str(answer))
            print ('====================================== \n Calculation completed! Result sent! \n======================================')
        except:
            print ('Invalid input!')
            sendAnswer = ('Invalid input!')


        if not data:
            break

        s_sock.send(str.encode(sendAnswer))

    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8828)) #port connnected
    print("waiting for client connection ...")
    s.listen(28)

    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('SOCKET ERROR!')

            except Exception as e:
                print("INTERRUPT!")
                print(e)
                sys.exit(1)
    finally:
           s.close()
