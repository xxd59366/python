#!/usr/bin/python3
import subprocess
import time
import os
import re


class StateCheck:
    def __init__(self, logfile):
        self.logfile = logfile
        self.date = time.strftime('%F %X')

    def log_check(self):
        if not os.path.isfile(self.logfile):
            f = open(self.logfile, 'w')
            f.close()

    def svc_check(self):
        self.log_check()
        # check nginx & rabbitmq
        svcs = {'nginx': '80', 'rabbitmq': '15672'}
        msgs = []
        for svc in svcs:
            com = 'ss -nlp | grep :' + svcs[svc]
            rs = subprocess.run(com, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if rs.returncode:
                msg = self.date + ' ' + 'Warning: ' + svc + ' is down.\n'
                msgs.append(msg)
                self.msg_to_adm(msg)
                self.repair_svcs(svc)

        # check mysql
        rs = subprocess.run(
            'mysql -hqmqz-production.cpckcb9jjals.rds.cn-north-1.amazonaws.com.cn -uevidence_management '
            '-pevidence_management -e ""',
            shell=True, stderr=subprocess.PIPE)
        if rs.returncode:
            msg = self.date + ' ' + 'Error: mysql svc is down.\n'
            msgs.append(msg)
            self.msg_to_adm(msg)

        # check msgSending
        rs = subprocess.run("ps aux | grep 'php72 /root/inotify' | grep -v 'grep'", shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        if rs.returncode:
            msg = self.date + ' ' + 'Warning: inotify svc is down.\n'
            msgs.append(msg)
            self.msg_to_adm(msg)
            self.repair_svcs('inotify')

        self.log_write(msgs)

    def log_write(self, msgs):
        # write into log
        with open(self.logfile, 'a') as f:
            for svc in msgs:
                f.writelines(svc)

    def redis_check(self):
        self.log_check()
        # check redis
        rs = subprocess.run('redis-cli ping', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if rs.returncode:
            msgs = []
            msg = self.date + ' ' + 'Error: redis svc is down.\n'
            self.msg_to_adm(msg)
            msgs.append(msg)
            self.log_write(msgs)

    def ping_test(self):
        self.log_check()
        rs = subprocess.run('ping -c 2 -i 0.5 -W 2 www.baidu.com', shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        if rs.returncode:
            msg = self.date + ' ' + 'Error: ping test has failed, pls check net state.\n'
            with open(self.logfile, 'a') as f:
                f.writelines(msg)
            self.msg_to_adm(msg)

    def msg_to_adm(self, msg):
        rs = subprocess.run(
            'curl -XGET "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww0d494d91aa7388ea&corpsecret=KPvcbSAYr2p86OLPOF1wAyQ-cbLvJZLjWB4zpjY60rk" 2> /dev/null',
            shell=True, stdout=subprocess.PIPE)
        if not rs.returncode:
            mystr = bytes.decode(rs.stdout)
            alist = re.split(',|:', mystr)
            access_token = alist[5][1:-1]
            info_post_dic = {
                "touser": "XuXiDong",
                "msgtype": "text",
                "agentid": 1000002,
                "text": {
                    "content": msg
                },
                "safe": 0
            }
            info_post = str(info_post_dic).replace("\'", '\"')  # 将数据格式中的单引号转化为json的双引号, 这一步非常重要
            topost = 'curl -XPOST "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token + '" -d ' + "'" + info_post + "'"
            rs = subprocess.run(topost, shell=True, stdout=subprocess.PIPE)

    def log_clean(self):
        self.log_check()
        lsize = os.path.getsize(self.logfile)
        if lsize >= 1048576:
            f = open(self.logfile, 'w')
            f.close()

    def repair_svcs(self, svc):
        msgs = []
        if svc == 'nginx':
            rs = subprocess.run('/usr/sbin/nginx -s reload', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if rs.returncode:
                msg = self.date + 'Error: Reload' + svc + 'failed, error is ' + rs.stderr + ', pls check the production host.'
                msgs.append(msg)
                self.msg_to_adm(msg)
        if svc == 'rabbitmq':
            rs = subprocess.run('rabbitmq-server &', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if rs.returncode:
                msg = self.date + 'Error: Reload' + svc + 'failed, error is ' + rs.stderr + ', pls check the production host.'
                msgs.append(msg)
                self.msg_to_adm(msg)
        if svc == 'inotify':
            rs = subprocess.run('sudo /root/inotify /var/sms', shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
            if rs.returncode:
                msg = self.date + 'Error: Reload' + svc + 'failed, error is ' + rs.stderr + ', pls check the production host.'
                msgs.append(msg)
                self.msg_to_adm(msg)

        self.log_write(msgs)


if __name__ == '__main__':
    s = StateCheck("/home/ec2-user/logs/state_check.log")
    s.svc_check()
    s.ping_test()
    s.log_clean()
