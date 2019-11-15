#!/usr/bin/python3
import subprocess
import time
import os
import re


class StateCheck:
    def __init__(self):
        self.logfile = "/home/ec2-user/logs/state_check.log"

    def svc_check(self):
        # check nginx & rabbitmq
        svc1 = {'nginx': '80', 'rabbitmq': '15672'}
        msgs = []
        for i in svc1:
            com = 'ss -nlp | grep :' + svc1[i] + ' &> /dev/null'
            rs = subprocess.run(com, shell=True)
            if rs.returncode:
                date = time.strftime('%F %X')
                msg = date + ' ' + 'Error: ' + i + ' is down.\n'
                msgs.append(msg)
                self.msg_to_adm(msg)

        # check mysql
        rs = subprocess.run(
            'mysql -hqmqz-production.cpckcb9jjals.rds.cn-north-1.amazonaws.com.cn -uevidence_management '
            '-pevidence_management -e ""',
            shell=True, stderr=subprocess.PIPE)
        if rs.returncode:
            date = time.strftime('%F %X')
            msg = date + ' ' + 'Error: mysql svc is down.\n'
            msgs.append(msg)
            self.msg_to_adm(msg)

        # write into log
        with open(self.logfile, 'a') as f:
            for i in msgs:
                f.writelines(i)

    def redis_check(self):
        # check redis
        rs = subprocess.run('redis-cli ping', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if rs.returncode:
            date = time.strftime('%F %X')
            msg = date + ' ' + 'Error: redis svc is down.\n'
            self.msg_to_adm(msg)
            with open(self.logfile, 'a') as f:
                f.writelines(msg)

    def ping_test(self):
        rs = subprocess.run('ping -c 2 -i 0.5 -W 2 www.baidu.com &> /dev/null', shell=True)
        if rs.returncode:
            date = time.strftime('%F %X')
            msg = date+' '+'Error: ping test has failed, pls check net state.\n'
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
            info_post = str(info_post_dic).replace("\'", '\"')
            topost = 'curl -XPOST "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token + '" -d ' + "'" + info_post + "'"
            rs = subprocess.run(topost, shell=True, stdout=subprocess.PIPE)

    def log_clean(self):
        lsize = os.path.getsize(self.logfile)
        if lsize >= 1048576:
            f = open(self.logfile, 'w')
            f.close()


if __name__ == '__main__':
    s = StateCheck()
    s.svc_check()
    s.ping_test()
    s.log_clean()
