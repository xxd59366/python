# use OOP
import sys
import re


# 节点对象,由ip和其他信息组成
class APoint:
    def __init__(self, ip, time, message):
        self.ip = ip
        self.info = (time, message)

    # browser方法返回每条消息的browser类型
    def browser(self):
        browser = re.search('(Chrome)|(Firefox)|(MSIE)', self.info[-1]).group()
        return browser


# 创建两个字典,一个记录主机信息,一个做browser次数统计
def cr_dicts(log_path):
    ip_dict = {}
    browser_dict = {}
    with open(log_path) as f:
        while True:
            arow = f.readline()
            if not arow:
                break

            ip = re.search('^(\d+\.){3}\d+', arow).group()
            time = re.search('\[.*\]', arow).group()[1:-1]
            message = re.search('".*', arow).group()
            row = APoint(ip, time, message)
            browser_dict[row.browser()] = browser_dict.get[row.browser(), 0] + 1
            if not ip_dict[row.ip]:
                ip_dict[row.ip] = [row.info]
            else:
                ip_dict[row.ip] += [row.info]

    return ip_dict, browser_dict


# 生成输出字典
def get_ipcount(ip_dict):
    ip_count = {}
    for ip in ip_dict:
        ip_count[ip] = len(ip_dict[ip])
    return ip_count


if __name__ == '__main__':
    log_path = sys.argv[1]
    ip_dict, browser_dict = cr_dicts(log_path)
    ip_count = get_ipcount(ip_dict)
    print(ip_count)
    print(browser_dict)
