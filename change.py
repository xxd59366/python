#!/bin/python3

import os
import pickle
import sys
import json
import re

from xml.etree.ElementTree import ElementTree as ET
from xml.dom import minidom


# 拉取目录下文件列表
def dir_walk(src_dir):
    filelist = []

    for path, folders, files in os.walk(src_dir):
        for each_file in files:
            if '.json' in each_file:
                filelist.append(each_file)
    # 保存文件清单
    with open('filelist', 'wb') as fobj:
        pickle.dump(filelist, fobj)
    return filelist


# 获取将json文件转化为字典对象
def get_info(fname):
    with open(fname, 'r', encoding='utf-8') as fobj:
        jinfo = fobj.read()
        data = json.loads(jinfo)
    return data

# 读入xml
def get_model(model):
    # 读入xml树结构
    with open(model, 'r', encoding='utf-8') as fobj:
        tree = ET()
        tree.parse(fobj)
    return tree

# 根据传入的json信息字典，修改xml模板后输出
def xml_create(tree, jinfo, fname, src_dir):
    model = tree.getroot()
    args = jinfo['arguments']
    extendParams = jinfo['extendParams']
    # 创建对应节点目录
    folderPath = extendParams['folderPath']
    dst_dir = os.path.join(src_dir.rstrip('/'), 'xmls', folderPath)

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)  
    # 对应xml信息
    classifyPath = model.findall('classifyPath')
    classifyPath[0].set('custom', extendParams['folderPath'])
    code = model.findall('code')
    code[0].text = extendParams['id']
    name = model.findall('name')
    usageType = model.findall('usageType')
    usageType[0].text = 'change'
    name[0].text = extendParams['name']
    paramContent = model.findall('paramContent')
    script = paramContent[0].findall('script')
    type = script[0].findall('type')
    type[0].text = extendParams['scriptType']

    fname = fname.split('.', 1)[0] + '.xml'
    fname = os.path.join(dst_dir, fname)
    tree.write(fname, encoding="utf-8", xml_declaration=True)
    return fname

def change_cdata(xml, jinfo):
    extendParams = jinfo['extendParams']
    args = jinfo['arguments']
    content = '<content><![CDATA[' + extendParams['excuteContent'] + ']]></content>'
    description = '<description><![CDATA[' + args[0]['description'] + ']]></description>'


    with open(xml , 'r', encoding='utf-8') as fobj:
        data = fobj.readlines()
        flag = 0
        for line in data:
            if extendParams.get('remark'):
                usage = '<usage><![CDATA[' + extendParams['remark'] + ']]></usage>'
                if re.findall(r'.*usage.*', line):
                    line = line.replace('<usage><![CDATA[]]></usage>', usage)
                    data[flag] = line
            if re.findall(r'.*content.*', line):
                line = line.replace('<content />', content)
                data[flag] = line
            elif re.findall(r'.*description.*', line):
                line = line.replace('<description />', description)
                data[flag] = line
            flag = flag + 1
        
    with open(xml , 'w', encoding='utf-8') as fobj:
        fobj.writelines(data)


if __name__ == '__main__':
    # 拉路径
    src_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]

    # 测试
    # 获取目录列表与xml模板
    flist = dir_walk(src_dir)
    xml = 'model.xml'
    tree = get_model(xml)
    for fname in flist:
        jinfo = get_info(fname)
        xml = xml_create(tree, jinfo, fname, src_dir)
        change_cdata(xml, jinfo)