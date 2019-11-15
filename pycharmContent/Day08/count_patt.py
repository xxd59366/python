"""用于统计一个文件中某些字段出现的次数"""
import re


def count_patt(fname, patt):
    patt_dict = {}
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                key = m.group()
                patt_dict[key] = patt_dict.get(key, 0) + 1
    return patt_dict


if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    br = 'Frefox|MSIE|Chrome'
    ip_count = count_patt(fname, ip)
    br_count = count_patt(fname, br)
    print(ip_count)
    print(br_count)
