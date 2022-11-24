import os, sys, time, random, threading, random, socket, select, datetime
import os
import sys
import random
import socket
import select
import datetime
import threading
import itertools
import threading
import time
import sys
import sys
import getpass
input('\033[36;1musername: ')
passwor = ''
while True:
    x = getpass.getpass()
    if x == '20012000':
        break
    sys.stdout.write('👊')
    passwor +=x

lambda text: text.decode('utf-8', 'ignore')

lock = threading.RLock(); os.system('cls' if os.name == 'nt' else 'clear')

def real_path(file_name):
    return os.path.dirname(os.path.abspath(__file__)) + file_name

def filter_array(array):
    for i in range(len(array)):
        array[i] = array[i].strip()
        if array[i].startswith('#'):
            array[i] = ''

    return [x for x in array if x]

def colors(value):
    patterns = {
        'R1' : '\033[31;1m', 'P1' : '\033[35;1m',
        'G1' : '\033[32;1m',  'CC' : '\033[0m',
    }

    for code in patterns:
        value = value.replace('[{}]'.format(code), patterns[code])

    return value

def log(value, status=' <<<>>> ', color='[CC]'):
    value = colors('{color}''[CC]''\033[0;36m{time} [CC]{color}{status} [CC]{color}{value}[CC]'.format(
        time=datetime.datetime.now().strftime('%I:%M %B %e %Y'),
        value=value,
        color=color,
        status=status
    ))
    with lock: print(value)

def log_replace(value, status='WARNING', color='[Y1]'):
    value = colors('{}{} ({})        [CC]\r'.format(color, status, value))
    with lock:
        sys.stdout.write(value)
        sys.stdout.flush()

class inject(object):
    def __init__(self, inject_host, inject_port):
        super(inject, self).__init__()

        self.inject_host = str(inject_host)
        self.inject_port = int(inject_port)

    def log(self, value, color='[G1]'):
        log(value, color=color)

    def start(self):
        try:
            socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_server.bind((self.inject_host, self.inject_port))
            socket_server.listen(1)
            frontend_domains = open(real_path('/edora')).readlines()
            frontend_domains = filter_array(frontend_domains)
            if len(frontend_domains) == 0:
                self.log('Frontend Domains not found. Please check edora.txt', color='[R1]')
                return
            self.log('!'.format(self.inject_host, self.inject_port))
            while True:
                socket_client, _ = socket_server.accept()
                socket_client.recv(65535)
                domain_fronting(socket_client, frontend_domains).start()
        except Exception as exception:
            self.log('ERROR!'.format(self.inject_host, self.inject_port), color='[R1]')

class domain_fronting(threading.Thread):
    def __init__(self, socket_client, frontend_domains):
        super(domain_fronting, self).__init__()

        self.frontend_domains = frontend_domains
        self.socket_tunnel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_client = socket_client
        self.buffer_size = 65535
        self.daemon = True

    def log(self, value, status='\033[0;30m', color='[CC]'):
        log(value, status=status, color=color)
        
    def handler(self, socket_tunnel, socket_client, buffer_size):
        sockets = [socket_tunnel, socket_client]
        timeout = 0
        while True:
            timeout += 1
            socket_io, _, errors = select.select(sockets, [], sockets, 3)
            if errors: break
            if socket_io:
                for sock in socket_io:
                    try:
                        data = sock.recv(buffer_size)
                        if not data: break
                        # SENT -> RECEIVED
                        elif sock is socket_client:
                            socket_tunnel.sendall(data)
                        elif sock is socket_tunnel:
                            socket_client.sendall(data)
                        timeout = 0
                    except: break
            if timeout == 30: break

    def run(self):
        try:
            self.proxy_host_port = random.choice(self.frontend_domains).split(':')
            self.proxy_host = self.proxy_host_port[0]
            self.proxy_port = self.proxy_host_port[1] if len(self.proxy_host_port) >= 2 and self.proxy_host_port[1] else "443"
            self.log('[P1]lost connection'.format(self.proxy_host, self.proxy_port))
            self.socket_tunnel.connect((str(self.proxy_host), int(self.proxy_port)))
            self.socket_client.sendall(b'HTTP/1.1 200 OK\r\n\r\n')
            self.handler(self.socket_tunnel, self.socket_client, self.buffer_size)
            self.socket_client.close()
            self.socket_tunnel.close()
            self.log('[G1]succes connection''[CC]'.format(self.proxy_host, self.proxy_port), color='[CC]')
        except OSError:
            self.log('\033[1;34m error scripts', color='[CC]')
        except :
            self.log('{} Not Responding'.format(self.proxy_host), color='[R1]')
            
done = False            
#animasi loading
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\033[1;32m\rLOADING ' + c)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\033[1;32m\rENTER!     ')

t = threading.Thread(target=animate)
t.start()

time.sleep(10)
done = True

#aditya nur ali
import time
 
load = '#'
count = 0
 
for x in range(101):
    time.sleep(0.0100)
    print(f'\033[1;31m\rLoading {x}% [{load}]', end='', flush=True)
    count += 1
    if count == 3:
        count = 0
        load += '#'
print('\n\033[1;32m https://adityanurali.blogspot.com')                  

#script berjalan
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.010)
mengetik('\033[0m')
mengetik('\033[0m')
mengetik('\033[1;31m<=========================================================>')
mengetik('\033[1;31m||   \033[0;35m      __    ____ \033[1;37m  ____  ____\033[0;35m  _  _    __           \033[1;31m||')
mengetik('\033[1;31m||   \033[1;32m     /__\  (  _ \ (_  _)\033[0;35m(_  _)( \/\033[1;32m )  /__\          \033[1;31m||')
mengetik('\033[1;31m||   \033[0;36m    /(__)\  )(_) ) _)(_   )\033[1;33m(   \  /  /(__)\         \033[1;31m||')
mengetik('\033[1;31m||   \033[0;31m   (__)(__)(____/ (____)\033[1;30m (__)  (__) (__)(__)        \033[1;31m||')
mengetik('\033[1;31m<=========================================================>')

#script berjalan
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.0100)
mengetik('\033[0m')
mengetik('\033[0m')
mengetik('\033[0m		  \033[44m    KRJ TEGAL JATENG   ')
mengetik('\033[0m		  \033[44m FREE PROVIDER INTERNET')
mengetik('\033[0;90m	      	       _           _')
mengetik('	      	     (_\         /_)')
mengetik('	      	       ))        ((')
mengetik('	      	     .-"""""""""-.')
mengetik('	      	 /^\/   _.   _.    \/^\'')
mengetik('	      	 \(     /__\ /__\   )/')
mengetik('	      	  \,    \o_/_\o_/  ,/')
mengetik('	      	    \      (_)      /')
mengetik('	      	     `-.  `===`  .-`')
mengetik('	      	      __)   -   (__')
mengetik('	      	    /     `~~~`    \\')
mengetik('	      	    /  /         \  \'')
mengetik('	      	    \ :           ; /')
mengetik('	      	     \|====(*)====|/')
mengetik('	      	      :           :')
mengetik('	      	       \         /')
mengetik('	      	     ___)=|   |=(___')
mengetik('	      	     {____/   \____}')

def main():
    print(colors('\n'.join([
     '[G1]LOCAL HOST:127.0.0.1','[CC]'
      '[G1]LOCAL PORT:8080','[CC]'
    ])))    
    inject('127.0.0.1', '8080').start()

if __name__ == '__main__':
    main()
#.....
