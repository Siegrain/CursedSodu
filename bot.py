import re
import time
import socket
import datetime
from db import DB


class Bot(object):

    def __init__(self, host, port, chan, nick, ident, realname):
        self.host = host
        self.port = port
        self.chan = chan
        self.nick = nick
        self.ident = ident
        self.realname = realname
        self.recv_buffer = ''
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.db = DB()

    def connect(self):
        self.socket.connect((self.host, self.port))
        self.send('NICK {}\r\n'.format(self.nick))
        self.send('USER {} {} bla :{}\r\n'.format(self.ident, self.host, self.realname))
        time.sleep(3)
        self.send('JOIN {}\r\n'.format(self.chan))

    def send(self, msg):
        self.socket.send(bytes('{}\r\n'.format(msg), 'UTF-8'))
        print('send: ' + msg)

    def recv(self):
        self.recv_buffer = self.socket.recv(1024).decode('UTF-8')
        temp = str.split(self.recv_buffer, '\n')

        for line in temp:
            try:
                line = str.rstrip(line)
                line = str.split(line)

                if (line[0] == 'PING'):
                    self.send('PONG {}'.format(line[1]))
            except:
                pass
        print('recv: ' + self.recv_buffer)

    def translate(self, m):
        # Parse IRC messages. Stolen from muirc (https://github.com/Gawen/muirc)

        IRC_RE = re.compile(r"(:(?P<nick>[^ !@]+)(\!(?P<user>[^ @]+))?(\@(?P<host>[^ ]+))? )?(?P<command>[^ ]+) (?P<params1>([^:]*))(?P<params2>(:.*)?)")
        
        if isinstance(m, str):
            # str -> msg
            m = IRC_RE.match(m.strip())

            if not m:
                return None

            m = m.groupdict()

            m["params"] = m.pop("params1").split()
            if m["params2"]:    m["params"] += [m["params2"][1:]]
            m.pop("params2")

            return m

        else:
            # msg -> str
            def gen():
                if m.get("nick", None):
                    yield ":" + m["nick"]
                    if m.get("user", None):   yield "!" + m["user"]
                    if m.get("host", None):   yield "@" + m["host"]
                    yield " "

                yield m["command"]
                
                if m.get("params", None):
                    for param in m["params"][:-1]:  yield " " + param

                    yield " "
                    if " " in m["params"][-1]:  yield ":"
                    yield m["params"][-1]

                yield ''

            return "".join(gen())

    def message(self, chan, msg):
        self.send('PRIVMSG {} :{}'.format(chan, msg))

    def log(self, msg):
        with open('log.txt', 'a') as f:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(now+str(msg)+'\n')

    def main(self):
        msg = self.translate(self.recv_buffer)
        self.log(msg)

        if msg['command'] == 'PRIVMSG':
            time.sleep(0.5)
            sender = msg['nick']
            channel = msg['params'][0].lower()
            message = msg['params'][1].lower()

            if self.nick.lower() in message:

                if 'rune' in message:
                    output = self.db.get(type='rune', amt=1)
                    if 'spread' in message:
                        output = self.db.get(type='rune', amt=3)

                elif 'spread' in message:
                        output = self.db.get(type='tarot', amt=3)

                elif 'yijing' in message or 'hexagram' in message:
                    output = self.db.get(type='yijing')

                else:
                    output = self.db.get(type='tarot', amt=1)

                self.message(channel, '{}: {}'.format(sender, output))

        print('msg: ' + str(msg))

bot = Bot(host='aesir.sorcery.net', port=9000, chan='#Siegrain',
          nick='CursedSodu', ident='CursedSodu', realname='CursedSodu')
bot.connect()

while 1:
    bot.recv()
    bot.main()
