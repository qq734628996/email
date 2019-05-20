#encoding:utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
import argparse

def send_email(**kw):
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    msg = MIMEText(kw['message'], 'plain', 'utf-8')
    msg['From'] = _format_addr('%s <%s>' % (kw['name'], kw['efrom']))
    msg['To'] = _format_addr('%s <%s>' % (kw['recipient_name'], kw['to']))
    msg['Subject'] = Header(kw['title'], 'utf-8').encode()

    server = smtplib.SMTP(kw['server'], 25)
    server.login(kw['efrom'], kw['password'])
    server.sendmail(kw['efrom'], [kw['to']], msg.as_string())
    server.quit()

def main():
    parser = argparse.ArgumentParser(description='Simple email sender.')
    parser.add_argument('-f', '--from', default='liukunxin1@163.com', dest='efrom')
    parser.add_argument('-p', '--password', default='liukunxin1')
    parser.add_argument('-t', '--to', default='liukunxin1@163.com')
    parser.add_argument('-s', '--server', help='smtp server', default='smtp.163.com')
    parser.add_argument('-m', '--message', default='hello smtp')
    parser.add_argument('-ti', '--title', default='title')
    parser.add_argument('-n', '--name', default='Anonymous')
    parser.add_argument('-rn', '--recipient_name', default='Dear')

    args = parser.parse_args()
    send_email(**vars(args))

if __name__ == "__main__":
    main()