import getpass
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from Tools.scripts.which import msg


def send_mail(host, password, sender, receivers, body, subject):
    msg = MIMEText(body, 'plain', 'utf8')
    msg['From'] = Header(sender, 'utf8')
    msg['To'] = Header(receivers[0], 'utf8')
    msg['Subject'] = Header(subject, 'utf8')

    # 发邮件：邮件服务器、发件人、收件人
    smtp = smtplib.SMTP()
    smtp.connect(host)
    # smtp.starttls()  # 使用证书的话需要打开
    smtp.login(sender, password)
    smtp.sendmail(sender, receivers, msg().as_bytes())


if __name__ == '__main__':
    sender = 'test@localtest.com'
    receivers = ['test@qq.com', 'test@163.com']
    server = 'smtp@126.com'
    password = getpass.getpass()
    body = 'Hello from python'
    subject = 'py mail test'
    send_mail(server, password, sender, receivers, body, subject)
